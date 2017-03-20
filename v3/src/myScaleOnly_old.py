import sys
import os
import time
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_scaleonly

from hx711 import HX711
stop_thread = False
class myScaleOnly(QWidget, ui_scaleonly.Ui_scaleOnly):
	sig_abort_thread = pyqtSignal()
	
	def __init__(self, mainWindow, name=None):
		super(myScaleOnly, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_tare.clicked.connect(lambda:self.handleBtn_tare())
		
		# set up thread that will update weight
	def start_thread():
		thread = QThread()
		getWeight = get_weight_thread()
		getWeight.finished[int].connect(self.onFinished)
		
		getWeight.moveToThread(self.thread)
		
		thread.started.connect(getWeight.work)
		thread.start()

	@pyqtSlot(int)
	def onFinished(self, i):
		self.lcd_number.display(int(i))
	
	def handleBtn_back(self, mainWindow):
		self.thread.quit()
		self.thread.wait()
		print("Is finished: %s" %self.thread.isFinished)
		stop_thread = True
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	
	def handleBtn_tare(self):
		scale.tare()

class get_weight_thread (QObject):
	finished = pyqtSignal(int)
	
	def __init__(self):
		#print ("get_weight_thread init")
		#super (self.__class__, self).__init__()
		super().__init__()
		self.__abort = False
	
	@pyqySlot()
	def work(self):
		#print ("get_weight_thread work")
		while stop_thread is not True:
			self.i = int(scale.get_weight(5))
			time.sleep(0.01)
			self.finished.emit(self.i)
			if stop_thread is True:
				break
	def abort(self):
		self.__abort = True
		
def cleanAndExit():
	scale.cleanAndExit()

# setup scale
scale = HX711(23,24)
# set reference unit is 435 for 5kg scale and 770 for 3kg scale
scale.set_reference_unit(770)
scale.reset()
scale.tare()
