import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src import myMainMenu, myAccountSetting
from ui import ui_usermenu

class myUserMenu(QWidget, ui_usermenu.Ui_userMenu):
	def __init__(self, mainWindow, name=None,layoutSetting=None, currentUserInfo=None):
		super(myUserMenu, self).__init__()
		self.setupUi(self)
		self.lbl_title.setText("Welcome %s !"%(currentUserInfo.firstname))
		self.btn_logout.clicked.connect(lambda:self.handleBtn_logout(mainWindow))
		self.btn_accountSetting.clicked.connect(lambda:self.handleBtn_accountSetting(mainWindow,currentUserInfo))

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
