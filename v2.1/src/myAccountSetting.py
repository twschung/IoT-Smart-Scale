import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src import myUserProfile
from ui import ui_accountsetting

class myAccountSetting(QWidget, ui_accountsetting.Ui_accountSetting):
	def __init__(self, mainWindow, name=None,layoutSetting=None, currentUserInfo=None):
		super(myAccountSetting, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
		self.btn_profile.clicked.connect(lambda:self.handleBtn_profile(mainWindow,currentUserInfo))

	def handleBtn_profile(self,mainWindow,currentUserInfo):
		self.widget = myUserProfile.myUserProfile(mainWindow=mainWindow,currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
