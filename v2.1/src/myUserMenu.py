import sys
sys.path.insert(0,"/home/pi/Desktop/v2.1/src")
sys.path.insert(0,"/home/pi/Desktop/v2.1/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import myMainMenu, myAccountSetting, myTrackingMenu, myFoodInformation
import ui_usermenu

class myUserMenu(QWidget, ui_usermenu.Ui_userMenu):
	def __init__(self, mainWindow, name=None,layoutSetting=None, currentUserInfo=None):
		super(myUserMenu, self).__init__()
		self.setupUi(self)
		self.lbl_title.setText("Welcome %s !"%(currentUserInfo.firstname))
		self.btn_logout.clicked.connect(lambda:self.handleBtn_logout(mainWindow))
		self.btn_accountSetting.clicked.connect(lambda:self.handleBtn_accountSetting(mainWindow,currentUserInfo))
		self.btn_myTracking.clicked.connect(lambda:self.handleBtn_myTracking(mainWindow,currentUserInfo))
		self.btn_scanFood.clicked.connect(lambda:self.handleBtn_scanFood(mainWindow,currentUserInfo))
	def handleBtn_accountSetting(self,mainWindow,currentUserInfo):
		self.widget = myAccountSetting.myAccountSetting(mainWindow=mainWindow,currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_logout(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myMainMenu.myMainMenu(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_myTracking(self,mainWindow,currentUserInfo):
		self.widget = myTrackingMenu.myTrackingMenu(mainWindow=mainWindow, currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_scanFood(self,mainWindow,currentUserInfo):
		self.widget = myFoodInformation.myFoodInformation(mainWindow=mainWindow, currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
