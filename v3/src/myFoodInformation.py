import sys
import os, shutil
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_foodinformation
import db_access, db_structure, ftp_access, myInfoPopUp, myFoodSuggestion
import time, math, datetime
from hx711 import HX711
from ad5933 import AD5933

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

import ml
import numpy as np
import obj_recognition

GPIO.setup(22, GPIO.OUT)
camera = PiCamera()
camera.resolution = (1024, 768)

i = 0
previous_weight = 0
current_weight = 0
run_scan = False

class myFoodInformation(QWidget, ui_foodinformation.Ui_foodInformation):
	NUM_THREADS = 1
	sig_abort_workers = pyqtSignal()
	def __init__(self, mainWindow, currentUserInfo, name=None, layoutSetting=None):
		global previous_weight
		previous_weight = 0
		run_scan = False
		super(myFoodInformation, self).__init__()
		msg = QMessageBox.information(self, 'Attention',"Please remove any itme on scale",QMessageBox.Ok)
		self.setupUi(self)
		self.foodInfo = None
		userDailyIntakeInfo = db_structure.userDailyIntakeStructure()
		self.btn_new.setText("Scan")
		if (layoutSetting == "guest"):
			self.btn_addIntake.setEnabled(False)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_new.clicked.connect(lambda:self.handleBtn_scan(mainWindow,currentUserInfo))
		self.btn_tare.clicked.connect(lambda:self.handleBtn_tare(mainWindow))
		self.btn_suggestion.setVisible(False)
		self.btn_addIntake.setVisible(False)
		# self.btn_suggestion.setEnabled(False)
		# self.btn_suggestion.clicked.connect(lambda:self.handleBtn_suggestion(mainWindow,currentUserInfo))
		# self.btn_addIntake.setEnabled(False)
		# self.btn_addIntake.clicked.connect(lambda:self.handleBtn_addIntake())

		self.foodWeight = 0
		camera.start_preview()
		camera.preview.alpha = 0
		msgbox = myInfoPopUp.myInfoPopUp("Wait....", "Camera initalising",self)
		msgbox.exec_()
		sleep(1)
		self.setUpBackgroundImage()
		msgbox.done(1)

		self.start_threads(mainWindow, currentUserInfo)

	def start_threads(self, mainWindow, currentUserInfo):
		global i
		i += 1
		#print('Starting thread %i' %i)
		self.__workers_done = 0
		self.__threads = []
		for idx in range(self.NUM_THREADS):
			worker = Worker(idx)
			thread = QThread()
			thread.setObjectName("get_weight_num"+str(idx)+"_"+str(i))
			self.__threads.append((thread,worker))

			worker.moveToThread(thread)

			# get progress messages from worker:
			worker.sig_step.connect(self.on_worker_step)
			worker.sig_done.connect(lambda: self.on_worker_done(mainWindow, currentUserInfo))

			# control worker:
			self.sig_abort_workers.connect(worker.abort)

			# get ready to start worker:
			thread.started.connect(worker.work)
			thread.start()  # this will emit 'started' and start thread's event loop

	def automated_scan(self, mainWindow, currentUserInfo):
		global run_scan
		if run_scan == True:
			self.handleBtn_scan(mainWindow, currentUserInfo)
		else:
			pass

	def print_weight_values(self):
		global current_weight, previous_weight
		print("current_weight = %i" %(current_weight))
		print("previous_weight = %i" %(previous_weight))
	def compare(self):
		global current_weight, previous_weight, run_scan
		if current_weight == previous_weight and current_weight > 0:
			run_scan = True
			self.abort_workers()
		elif current_weight != previous_weight:
			#self.print_weight_values()
			previous_weight = current_weight

	@pyqtSlot(int, str)
	def on_worker_step(self, worker_id: int, data: str):
		self.lcd_number.display(str(data))
		#print('worker #%i : %s' %(worker_id, data))
		#self.progress.append('{}: {}'.format(worker_id, data))
		global current_weight, previous_weight
		current_weight = int(data)
		self.compare()

	@pyqtSlot()
	def on_worker_done(self, mainWindow, currentUserInfo):
		self.__workers_done += 1
		self.automated_scan(mainWindow, currentUserInfo)

	@pyqtSlot()
	def abort_workers(self):
		#print('UI.abort_workers - Asking each worker to abort')
		#Worker.abort(self)
		self.sig_abort_workers.emit()
		for thread, worker in self.__threads:  # note nice unpacking by Python, avoids indexing
			thread.quit()  # this will quit **as soon as thread event loop unblocks**
			thread.wait()  # <- so you need to wait for it to *actually* quit
		# even though threads have exited, there may still be messages on the main thread's
		# queue (messages that threads emitted before the abort):
		#print('UI.abort_workers - All threads exited')

	def handleBtn_back(self,mainWindow):
		global run_scan
		run_scan = False
		camera.stop_preview()
		self.abort_workers()
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())

	def handleBtn_scan(self,mainWindow,currentUserInfo):
		# add camera modules stuff here
		self.setUpForgroundImage()
		imageFeature = obj_recognition.main("forground.jpg", "background.jpg")
		if (imageFeature[1]==False):
			msg = QMessageBox.information(self, 'Error',"Food not detected! (No object is detected)",QMessageBox.Ok)
			return
		clf = ml.classifier()
		clf.load()
		clfResult = clf.predict(imageFeature[0])
		self.clfProb = clf.predict_prob(imageFeature[0])
		foodID = clfResult[0]

		self.foodWeight = int(scale.get_weight(5))
		self.btn_addIntake.setEnabled(False)
		if(currentUserInfo==None):
			userId=0
		else:
			userId=currentUserInfo.id
		if(self.foodWeight<=0):
			msg = QMessageBox.information(self, 'Error',"Food not detected! (Item mass is equal or less than 0g)",QMessageBox.Ok)
		else:
			self.widget = myFoodSuggestion.myFoodSuggestion(mainWindow, currentUserInfo, self.clfProb, self.foodWeight, self)
			mainWindow.central_widget.addWidget(self.widget)
			mainWindow.central_widget.setCurrentWidget(self.widget)

		# BioImpedance Stuff here
		gain_factor = 5.12e-10 #5.75882e-10#4.902e-11 #1.013e-9
		system_phase = 1.95 #rads
		meter = AD5933(gain_factor, system_phase, 10)
		meter.SET_OPERATING_RANGE(1)
		readings = meter.MEASURE_IMPEDANCE()
		percentage = self.getFatPercentage(self.foodWeight, readings[2])
		print("Fat Percentage %i%" %percentage)
		#self.lbl_(newlab).setText("Fat Percentage " + str(percentage) +"%")

	def handleBtn_tare(self, mainWindow):
		scale.reset()
		scale.tare()

	def handleBtn_addIntake(self):
		db_access.user_addNewFoodIntake(self.foodInfo)
		forgroundFilePath, backgroundFilePath = ftp_access.generateExisitingItemFilePath(self.foodInfo.foodid)
		shutil.copyfile(os.path.join(os.getcwd(),"background.jpg"),backgroundFilePath)
		shutil.copyfile(os.path.join(os.getcwd(),"forground.jpg"),forgroundFilePath)
		msg = QMessageBox.information(self, 'Added',"Food item has been added to your intake",QMessageBox.Ok)
		self.btn_addIntake.setEnabled(False)
		self.btn_suggestion.setEnabled(False)

	def handleBtn_suggestion(self, mainWindow, currentUserInfo):
		self.btn_addIntake.setEnabled(False)
		self.btn_suggestion.setEnabled(False)
		self.widget = myFoodSuggestion.myFoodSuggestion(mainWindow, currentUserInfo, self.clfProb, self.foodWeight)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)

	def setUpBackgroundImage(self):
		GPIO.output(22,True)
		camera.capture("background.jpg")
		GPIO.output(22,False)

	def setUpForgroundImage(self):
		GPIO.output(22,True)
		camera.capture("forground.jpg")
		GPIO.output(22,False)

	def getFatPercentage(self, weight, R):
		print(weight)
		print(R)
		self.intercept = (-108.81)
		self.coeff_weight = weight * 0.114573491
		self.coeff_logR2 = (math.log10(R)**2)*4.602619168
		self.coeff_R = R*(-7.814e-5)
		self.coeff = self.intercept + self.coeff_weight + self.coeff_logR2 + self.coeff_R
		fat_perc = int(self.coeff/weight*100)
		return fat_perc

	def updateFoodInfo(self,self_e,foodID,currentUserInfo):
		self=self_e
		if(currentUserInfo==None):
			userId=0
		else:
			userId=currentUserInfo.id
		s = str(foodID)+".jpg"
		self.pic = QPixmap(currentDir+'/imageSample/'+s)
		self.scaledPic = self.pic.scaled(self.lbl_foodPic.width(), self.lbl_foodPic.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
		self.lbl_foodPic.setPixmap(self.scaledPic)
		self.foodInfo = db_access.food_getActualInfo(userId,str(foodID),str(self.foodWeight))
		self.lbl_foodName.setText(self.foodInfo.fooddescription)
		self.lbl_evergyVal.setText(str(round(self.foodInfo.energy,1))) #typo on the ui file, use 'evergy'
		self.lbl_proteinVal.setText(str(round(self.foodInfo.protein,1)))
		self.lbl_sugarVal.setText(str(round(self.foodInfo.sugars,1)))
		self.lbl_fibreVal.setText(str(round(self.foodInfo.fibre,1)))
		self.lbl_fatVal.setText(str(round(self.foodInfo.fat,1)))
		self.lbl_saltVal.setText(str(round(self.foodInfo.salt,1)))
		if(currentUserInfo!=None):
			db_access.user_addNewFoodIntake(self.foodInfo)
			forgroundFilePath, backgroundFilePath = ftp_access.generateExisitingItemFilePath(self.foodInfo.foodid)
			shutil.copyfile(os.path.join(os.getcwd(),"background.jpg"),backgroundFilePath)
			shutil.copyfile(os.path.join(os.getcwd(),"forground.jpg"),forgroundFilePath)
			# msg = QMessageBox.information(self, 'Added',"Food item has been added to your intake",QMessageBox.Ok)


class Worker (QObject):
	sig_step = pyqtSignal(int, str)
	sig_done = pyqtSignal(int)
	def __init__(self, id: int, ):
		super().__init__()
		self.__id = id
		self.__abort = False

	@pyqtSlot()
	def work(self):
		thread_name = QThread.currentThread().objectName()
		thread_id = int(QThread.currentThreadId())  # cast to int() is necessary

		#while self.__abort is not True:
			#self.current_weight = int(scale.get_weight(5))
			#self.sig_step.emit(self.__id, str(self.current_weight))
			#if self.__abort is True:
				#self.sig_msg.emit('Worker #{} aborting work'.format(self.__id))
				##self.sig_done.emit(self.__id)
				#break
		### This entire block is the key
		while True:
			#print("Worker.work(in while) - self.__abort = %s" %self.__abort)
			time.sleep(0.01)
			#self.sig_step.emit(self.__id, 'step ' + str(step))
			self.current_weight = int(scale.get_weight(5))
			self.sig_step.emit(self.__id, str(self.current_weight))
			## check if we need to abort the loop; need to process events to receive signals;
			app.processEvents()  # this could cause change to self.__abort
			if self.__abort == True:
				## note that "step" value will not necessarily be same for every thread
				#.sig_msg.emit('Worker #{} aborting work at step {}'.format(self.__id, step))
				#print("Thread: %s ended" %thread_name)
				break
		###
		self.sig_done.emit(self.__id)

	def abort(self):
		self.__abort = True
		#print("Setting self.__abort to True\n\tWorker.abort - self.__abort = %s" %self.__abort)
		#self.sig_msg.emit('worker #{} notified to abort'.format(self.__id))

# setup scale
scale = HX711(23,24)
# set reference unit is 435 for 5kg scale and 770 for 3kg scale
scale.set_reference_unit(435)
scale.reset()
scale.tare()

app = QApplication([])
