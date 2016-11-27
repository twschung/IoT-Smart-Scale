import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_loginmenu
from src import myUserSetup

class myLoginMenu(QWidget, ui_loginmenu.Ui_loginMenu):
	def __init__(self, mainWindow, name=None):
		super(myLoginMenu, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_newLogin.clicked.connect(lambda:self.handleBtn_newLogin(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_newLogin(self, mainWindow):
		self.widget = myUserSetup.myUserSetup(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
