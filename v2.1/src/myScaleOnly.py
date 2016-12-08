import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_scaleonly

from hx711 import HX711

class myScaleOnly(QWidget, ui_scaleonly.Ui_scaleOnly):
	def __init__(self, mainWindow, name=None):
		super(myScaleOnly, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_tare.clicked.connect(lambda:self.handleBtn_tare())
		
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
	
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	
	def handleBtn_tare(self):
		scale.tare()

class get_weight_thread (QObject):
	finished = pyqtSignal(int)
	
	def __init__(self):
		print ("get_weight_thread init")
		#super (self.__class__, self).__init__()
		super().__init__()
	
	def work(self):
		print ("get_weight_thread work")
		while True:
			self.i = int(scale.get_weight(5))
			self.finished.emit(self.i)

# setup scale
scale = HX711(23,24)
scale.set_reference_unit(770)
scale.reset()
scale.tare()
