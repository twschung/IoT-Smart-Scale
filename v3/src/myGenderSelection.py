import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_genderSelection
import myUserSetup, myUserEdit

class myGenderSelection(QWidget, ui_genderSelection.Ui_genderSelection):
	def __init__(self, mainWindow, name=None, layoutSetting=None, dataStruc=None):
		super(myGenderSelection, self).__init__()
		self.setupUi(self)
		self.btn_male.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/male.png")))
		self.btn_male.setIconSize(QSize(130,130))
		self.btn_female.setIcon(QIcon(QPixmap(os.getcwd()+ "/ui/icon/female.png")))
		self.btn_female.setIconSize(QSize(130,130))
		if (layoutSetting == "newUser_gender"):
			self.lbl_title.setText("New User Setup Wizard")
			self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
			self.btn_male.clicked.connect(lambda:self.handleBtn_male_new(mainWindow,dataStruc))
			self.btn_female.clicked.connect(lambda:self.handleBtn_female_new(mainWindow,dataStruc))
		if (layoutSetting == "editUser_gender"):
			self.lbl_title.setText("Editing user details")
			self.btn_back.setEnabled(False)
			self.btn_male.clicked.connect(lambda:self.handleBtn_male_edit(mainWindow,dataStruc))
			self.btn_female.clicked.connect(lambda:self.handleBtn_female_edit(mainWindow,dataStruc))
	def handleBtn_male_new(self, mainWindow, dataStruc):
		dataStruc.gender = "m"
		myUserSetup.myUserSetup.newUser_email(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handleBtn_female_new(self, mainWindow, dataStruc):
		dataStruc.gender = "f"
		myUserSetup.myUserSetup.newUser_email(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handleBtn_male_edit(self, mainWindow, dataStruc):
		dataStruc.gender = "m"
		myUserEdit.myUserEdit.editUser_firstname(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
	def handleBtn_female_edit(self, mainWindow, dataStruc):
		dataStruc.gender = "f"
		myUserEdit.myUserEdit.editUser_firstname(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
