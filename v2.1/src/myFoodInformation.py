import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_foodinformation

class myFoodInformation(QWidget, ui_foodinformation.Ui_foodInformation):
	def __init__(self, mainWindow, name=None, layoutSetting=None):
		super(myFoodInformation, self).__init__()
		self.setupUi(self)
		if (layoutSetting == "guest"):
			self.btn_back.clicked.connect(lambda:self.handleBtn_back_guest(mainWindow))
			self.btn_addIntake.setEnabled(False)
	def handleBtn_back_guest(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
