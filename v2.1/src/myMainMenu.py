import sys
sys.path.insert(0,"/home/pi/Desktop/v2.1/src")
sys.path.insert(0,"/home/pi/Desktop/v2.1/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import myLoginMenu, myFoodInformation, myScaleOnly, myUserSetup
import ui_mainmenu

class myMainMenu(QWidget, ui_mainmenu.Ui_mainMenu):
	def __init__(self, mainWindow, name=None):
		super(myMainMenu, self).__init__()
		self.setupUi(self)
		self.btn_login.clicked.connect(lambda:self.handleBtn_login(mainWindow))
		self.btn_guest.clicked.connect(lambda:self.handleBtn_guest(mainWindow))
		self.btn_scaleOnly.clicked.connect(lambda:self.handleBtn_scaleOnly(mainWindow))
		self.btn_userSetup.clicked.connect(lambda:self.handleBtn_userSetup(mainWindow))
	def handleBtn_login(self, mainWindow):
		self.widget = myLoginMenu.myLoginMenu(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_guest(self, mainWindow):
		self.widget = myFoodInformation.myFoodInformation(mainWindow,currentUserInfo=None,layoutSetting = "guest")
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_scaleOnly(self, mainWindow):
		self.widget = myScaleOnly.myScaleOnly(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_userSetup(self, mainWindow):
		myUserSetup.myUserSetup(mainWindow)
