import sys
import os
import datetime, time
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import ui_scaleonly

from hx711 import HX711
i = 0

class myScaleOnly(QWidget, ui_scaleonly.Ui_scaleOnly):
	NUM_THREADS = 1
	sig_abort_workers = pyqtSignal()
	def __init__(self, mainWindow, name=None):
		super(myScaleOnly, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_tare.clicked.connect(lambda:self.handleBtn_tare())
		self.start_threads()

	def start_threads(self):
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
			worker.sig_done.connect(self.on_worker_done)

			# control worker:
			self.sig_abort_workers.connect(worker.abort)

			# get ready to start worker:
			thread.started.connect(worker.work)
			thread.start()  # this will emit 'started' and start thread's event loop

	@pyqtSlot(int, str)
	def on_worker_step(self, worker_id: int, data: str):
		self.lcd_number.display(str(data))
		#print('worker #%i : %s' %(worker_id, data))
		#self.progress.append('{}: {}'.format(worker_id, data))

	@pyqtSlot(int)
	def on_worker_done(self, worker_id):
		#print('worker %i done' %(worker_id))
		self.__workers_done += 1

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

	def handleBtn_back(self, mainWindow):
		self.abort_workers()
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())

	def handleBtn_tare(self):
		scale.tare()

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

def cleanAndExit():
	HX711.cleanAndExit()

# setup scale
scale = HX711(23,24)
# set reference unit is 435 for 5kg scale and 770 for 3kg scale
scale.set_reference_unit(770)
scale.reset()
scale.tare()
scale.tare()

app = QApplication([])
