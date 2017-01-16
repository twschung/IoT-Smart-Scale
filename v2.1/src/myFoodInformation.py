import sys
import os, shutil
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_foodinformation
import db_access, db_structure, ftp_access
import time
from hx711 import HX711

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

import ml
import numpy as np
import obj_recognition

GPIO.setup(17, GPIO.OUT)
camera = PiCamera()
camera.resolution = (1024, 768)

class myFoodInformation(QWidget, ui_foodinformation.Ui_foodInformation):
	def __init__(self, mainWindow, currentUserInfo, name=None, layoutSetting=None):
		super(myFoodInformation, self).__init__()
		self.setupUi(self)
		self.foodInfo = None
		userDailyIntakeInfo = db_structure.userDailyIntakeStructure()
		self.btn_new.setText("Scan")
		if (layoutSetting == "guest"):
			self.btn_addIntake.setEnabled(False)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_new.clicked.connect(lambda:self.handleBtn_scan(mainWindow,currentUserInfo))
		self.btn_tare.clicked.connect(lambda:self.handleBtn_tare(mainWindow))
		self.btn_addIntake.setEnabled(False)
		self.btn_addIntake.clicked.connect(lambda:self.handleBtn_addIntake())
		self.foodWeight = 0
		self.setUpBackgroundImage()
		# set up thread that will update weight
		self.thread = QThread()
		self.getWeight = get_weight_thread()
		self.getWeight.finished[int].connect(self.onFinished)
		self.getWeight.moveToThread(self.thread)
		self.thread.started.connect(self.getWeight.work)
		self.thread.start()

	@pyqtSlot(int)
	def onFinished(self, i):
		self.lcd_number.display(int(i))
	def handleBtn_back(self,mainWindow):
		self.thread.terminate()
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_scan(self,mainWindow,currentUserInfo):
		# add camera modules stuff here
		self.setUpForgroundImage()
		imageFeature = obj_recognition.main("forground.jpg", "background.jpg")
		clf = ml.classifier()
		clf.load()
		clfResult = clf.predict(imageFeature)
		foodID = clfResult[0]
		self.foodWeight = int(scale.get_weight(5))
		self.btn_addIntake.setEnabled(False)
		if(currentUserInfo==None):
			userId=0
		else:
			userId=currentUserInfo.id
		if(self.foodWeight==0):
			msg = QMessageBox.information(self, 'Error',"Food not detected! (Item mass is 0g)",QMessageBox.Ok)
		else:
			self.foodInfo = db_access.food_getActualInfo(userId,str(foodID),str(self.foodWeight))
			self.lbl_evergyVal.setText(str(self.foodInfo.energy)) #typo on the ui file, use 'evergy'
			self.lbl_proteinVal.setText(str(self.foodInfo.protein))
			self.lbl_sugarVal.setText(str(self.foodInfo.sugars))
			self.lbl_fibreVal.setText(str(self.foodInfo.fibre))
			self.lbl_fatVal.setText(str(self.foodInfo.fat))
			self.lbl_saltVal.setText(str(self.foodInfo.salt))
			if(currentUserInfo==None):
				self.btn_addIntake.setEnabled(False)
			else:
				self.btn_addIntake.setEnabled(True)
	def handleBtn_tare(self, mainWindow):
		# add tare stuff here
		scale.tare()
	def handleBtn_addIntake(self):
		db_access.user_addNewFoodIntake(self.foodInfo)
		msg = QMessageBox.information(self, 'Added',"Food item has been added to your intake",QMessageBox.Ok)
		self.btn_addIntake.setEnabled(False)

	def setUpBackgroundImage(self):
		camera.start_preview()
		GPIO.output(17,True)
		# msg = QMessageBox.information(self, 'Wait....',"Camera initalising",QMessageBox.Ok)
		sleep(1)
		camera.capture("background.jpg")
		camera.stop_preview()
		GPIO.output(17,False)

	def setUpForgroundImage(self):
		camera.start_preview()
		GPIO.output(17,True)
		# msg = QMessageBox.information(self, 'Wait....',"Camera initalising",QMessageBox.Ok)
		sleep(1)
		camera.capture("forground.jpg")
		camera.stop_preview()
		GPIO.output(17,False)
		(forgroundFilePath,backgroundFilePath) =  ftp_access.generateExisitingItemFilePath()
		shutil.copyfile('forground.jpg',forgroundFilePath)
		shutil.copyfile('background.jpg',backgroundFilePath)


class get_weight_thread (QObject):
	finished = pyqtSignal(int)

	def __init__(self):
		#print ("get_weight_thread init")
		#super (self.__class__, self).__init__()
		super().__init__()

	def work(self):
		#print ("get_weight_thread work")
		while True:
			self.i = int(scale.get_weight(5))
			self.finished.emit(self.i)

# setup scale
scale = HX711(23,24)
# set reference unit is 435 for 5kg scale and 770 for 3kg scale
scale.set_reference_unit(435)
scale.reset()
scale.tare()
