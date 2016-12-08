import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import myUserProfile, myUserEdit, myGoal
import ui_accountsetting

class myAccountSetting(QWidget, ui_accountsetting.Ui_accountSetting):
	def __init__(self, mainWindow, name=None,layoutSetting=None, currentUserInfo=None):
		super(myAccountSetting, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
		self.btn_passcode.clicked.connect(lambda:self.handleBtn_passcode(mainWindow,currentUserInfo))
		self.btn_profile.clicked.connect(lambda:self.handleBtn_profile(mainWindow,currentUserInfo))
		self.btn_goal.clicked.connect(lambda:self.handleBtn_goal(mainWindow,currentUserInfo))
	def handleBtn_passcode(self,mainWindow,currentUserInfo):
		myUserEdit.myUserEdit.editUser_oldPasscode(self, mainWindow=mainWindow,currentUserInfo=currentUserInfo)
	def handleBtn_profile(self,mainWindow,currentUserInfo):
		self.widget = myUserProfile.myUserProfile(mainWindow=mainWindow,currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_goal(self, mainWindow, currentUserInfo):
		self.widget = myGoal.myGoal(mainWindow, currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
