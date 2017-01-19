import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import myUserEdit,myUserLogin
import ui_passcodeMenu

class myPasscodeMenu(QWidget, ui_passcodeMenu.Ui_passcodeMenu):
	def __init__(self, mainWindow, name=None,layoutSetting=None, currentUserInfo=None):
		super(myPasscodeMenu, self).__init__()
		self.setupUi(self)
		self.btn_back.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/back.png")))
		self.btn_back.setIconSize(QSize(130,130))
		self.btn_fingerprint.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/fingerprint.png")))
		self.btn_fingerprint.setIconSize(QSize(130,130))
		self.btn_changePasscode.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/passcode.png")))
		self.btn_changePasscode.setIconSize(QSize(130,130))
		self.btn_rmUsrFromMenu.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/removeUser.png")))
		self.btn_rmUsrFromMenu.setIconSize(QSize(130,130))
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow,currentUserInfo))
		self.btn_fingerprint.clicked.connect(lambda:self.handleBtn_fingerprint(mainWindow,currentUserInfo))
		self.btn_changePasscode.clicked.connect(lambda:self.handleBtn_changePasscode(mainWindow,currentUserInfo))
		self.btn_rmUsrFromMenu.clicked.connect(lambda:self.handleBtn_rmUsrFromMenu(mainWindow,currentUserInfo))
	def handleBtn_back(self,mainWindow,currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_changePasscode(self,mainWindow,currentUserInfo):
		myUserEdit.myUserEdit.editUser_newPasscode(self,mainWindow=mainWindow,currentUserInfo=currentUserInfo)
	def handleBtn_fingerprint(self,mainWindow,currentUserInfo):
		self.widget = myUserProfile.myUserProfile(mainWindow=mainWindow,currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_rmUsrFromMenu(self, mainWindow, currentUserInfo):
		myUserLogin.myUserLogin.forgetUser(self, currentUserInfo=currentUserInfo)
