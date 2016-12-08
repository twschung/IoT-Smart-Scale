import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_loginmenu
import myUserLogin, myPasscode
import db_structure
import numpy as np

class myLoginMenu(QWidget, ui_loginmenu.Ui_loginMenu):
	def __init__(self, mainWindow, name=None):
		super(myLoginMenu, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_newLogin.clicked.connect(lambda:self.handleBtn_newLogin(mainWindow))
		self.btn_user1.clicked.connect(lambda:self.handleBtn_user(mainWindow=mainWindow,userNum=0))
		self.btn_user2.clicked.connect(lambda:self.handleBtn_user(mainWindow=mainWindow,userNum=1))
		self.btn_user3.clicked.connect(lambda:self.handleBtn_user(mainWindow=mainWindow,userNum=2))
		self.btn_user4.clicked.connect(lambda:self.handleBtn_user(mainWindow=mainWindow,userNum=3))
		self.btn_user5.clicked.connect(lambda:self.handleBtn_user(mainWindow=mainWindow,userNum=4))
		self.btn_user6.clicked.connect(lambda:self.handleBtn_user(mainWindow=mainWindow,userNum=5))
		self.processConfig()
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_newLogin(self, mainWindow):
		myUserLogin.myUserLogin(mainWindow, newUser=True)
	def handleBtn_user(self, mainWindow, userNum):
		self.config = np.load('config.npy').item()
		myUserLogin.myUserLogin.loginUser_passcode(self, mainWindow=mainWindow, currentUserInfo=self.config['expUsr'][userNum], newUser=False)
	def processConfig(self):
		try:
			self.config = np.load('config.npy').item()
		except:
			blankUsrInfo = db_structure.userDataStructure()
			expUsr = [blankUsrInfo,blankUsrInfo,blankUsrInfo,blankUsrInfo,blankUsrInfo,blankUsrInfo]
			self.config = {'expUsr':expUsr}
			np.save('config.npy', self.config)
		finally:
			if (self.config['expUsr'][0].id != ""):
				self.btn_user1.setEnabled(True)
				self.btn_user1.setText(self.config['expUsr'][0].firstname + " " + self.config['expUsr'][0].lastname)
			if (self.config['expUsr'][1].id != ""):
				self.btn_user2.setEnabled(True)
				self.btn_user2.setText(self.config['expUsr'][1].firstname + " " + self.config['expUsr'][1].lastname)
			if (self.config['expUsr'][2].id != ""):
				self.btn_user3.setEnabled(True)
				self.btn_user3.setText(self.config['expUsr'][2].firstname + " " + self.config['expUsr'][2].lastname)
			if (self.config['expUsr'][3].id != ""):
				self.btn_user4.setEnabled(True)
				self.btn_user4.setText(self.config['expUsr'][3].firstname + " " + self.config['expUsr'][3].lastname)
			if (self.config['expUsr'][4].id != ""):
				self.btn_user5.setEnabled(True)
				self.btn_user5.setText(self.config['expUsr'][4].firstname + " " + self.config['expUsr'][4].lastname)
			if (self.config['expUsr'][5].id != ""):
				self.btn_user6.setEnabled(True)
				self.btn_user6.setText(self.config['expUsr'][5].firstname + " " + self.config['expUsr'][5].lastname)
