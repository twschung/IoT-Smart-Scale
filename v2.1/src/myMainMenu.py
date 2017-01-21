import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import myLoginMenu, myFoodInformation, myScaleOnly, myUserSetup, myInfoPopUp
import ftp_access
import ui_mainmenu

class myMainMenu(QWidget, ui_mainmenu.Ui_mainMenu):
	def __init__(self, mainWindow, name=None):
		super(myMainMenu, self).__init__()
		self.setupUi(self)
		self.btn_login.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/login.png")))
		self.btn_login.setIconSize(QSize(130,130))
		self.btn_guest.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/guest.png")))
		self.btn_guest.setIconSize(QSize(130,130))
		self.btn_scaleOnly.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/scale.png")))
		self.btn_scaleOnly.setIconSize(QSize(130,130))
		self.btn_userSetup.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/userSetup.png")))
		self.btn_userSetup.setIconSize(QSize(130,130))
		self.btn_close.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/exit.png")))
		self.btn_close.setIconSize(QSize(60,60))
		self.btn_update.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/update.png")))
		self.btn_update.setIconSize(QSize(60,60))
		self.btn_login.clicked.connect(lambda:self.handleBtn_login(mainWindow))
		self.btn_guest.clicked.connect(lambda:self.handleBtn_guest(mainWindow))
		self.btn_scaleOnly.clicked.connect(lambda:self.handleBtn_scaleOnly(mainWindow))
		self.btn_userSetup.clicked.connect(lambda:self.handleBtn_userSetup(mainWindow))
		self.btn_close.clicked.connect(lambda:self.handleBtn_close())
		self.btn_update.clicked.connect(lambda:self.handleBtn_systemUpdate())
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
	def handleBtn_close(self):
		quit_msg = "Are you sure you want to exit the program?"
		reply = QMessageBox.question(self,'Message',quit_msg,QMessageBox.Yes,QMessageBox.No)
		if(reply==QMessageBox.Yes):
			sys.exit()
		else:
			pass
	def handleBtn_systemUpdate(self):
		# msg = QMessageBox.information(self, 'System Update',"System and database being updated",QMessageBox.Ok)
		# msgbox = QMessageBox(self)
		# msgbox.setIcon(QMessageBox.Information)
		# msgbox.setText("System and database being updated")
		# msgbox.setWindowModality(Qt.NonModal)
		# msgbox.open()
		msgbox = myInfoPopUp(self,title = "System Updating...", message = "System and database being updated")
		msgbox.show()
		ftp_access.updateImageSample()
		ftp_access.updateML()
		ftp_access.updatelocalDB()
		ftp_access.uploadImageHistory()
		msgbox.done(1)
