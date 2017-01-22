import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_loginmenu
import myUserLogin, myPasscode, fingerprint
import db_structure
import numpy as np

class myLoginMenu(QWidget, ui_loginmenu.Ui_loginMenu):
	def __init__(self, mainWindow, name=None):
		super(myLoginMenu, self).__init__()
		self.setupUi(self)
		self.btn_back.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/back.png")))
		self.btn_back.setIconSize(QSize(65,65))
		self.btn_newLogin.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/passcode.png")))
		self.btn_newLogin.setIconSize(QSize(65,65))
		self.btn_fingerprint.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/fingerprint.png")))
		self.btn_fingerprint.setIconSize(QSize(65,65))
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_newLogin.clicked.connect(lambda:self.handleBtn_newLogin(mainWindow))
		self.btn_fingerprint.clicked.connect(lambda:self.handleBtn_fingerprint(mainWindow))
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
	def handleBtn_fingerprintLogin(self,mainWindow):
		config = np.load('config.npy').item()
		try:
			fpUsr = config['fpUsr']
		except:
			fpUsr = []
		finally:
			fpResult = fingerprint.searchFinger()
			if (fpResult[0]==True):
				for i in range(0,len(fpUsr)):
					if (fpUsr[i].fpid == fpResult[1]):
						print (fpUsr[i].username)
						print (fpUsr[i].password)
						break

	def handleBtn_user(self, mainWindow, userNum):
		self.config = np.load('config.npy').item()
		myUserLogin.myUserLogin.loginUser_passcode(self, mainWindow=mainWindow, currentUserInfo=self.config['expUsr'][userNum], newUser=False)
	def processConfig(self):
		try:
			self.config = np.load('config.npy').item()
			try:
				temp = self.config['expUsr']
			except:
				blankUsrInfo = db_structure.userDataStructure()
				expUsr = [blankUsrInfo,blankUsrInfo,blankUsrInfo,blankUsrInfo,blankUsrInfo,blankUsrInfo]
				self.config = {'expUsr':expUsr}
				np.save('config.npy', self.config)
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
