import sys
sys.path.insert(0,"/home/pi/Desktop/v2.1/src")
sys.path.insert(0,"/home/pi/Desktop/v2.1/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_scaleonly

class myScaleOnly(QWidget, ui_scaleonly.Ui_scaleOnly):
	def __init__(self, mainWindow, name=None):
		super(myScaleOnly, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
