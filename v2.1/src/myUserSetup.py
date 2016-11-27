import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_usersetup
from src import myPasscode

class myUserSetup(QWidget, ui_usersetup.Ui_userSetup):
	def __init__(self, mainWindow, name=None):
		super(myUserSetup, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_sub.clicked.connect(lambda:self.handleBtn_sub(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_sub(self, mainWindow):
		self.widget = myPasscode.myPasscode(mainWindow,layoutSetting = "newPasscode")
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
