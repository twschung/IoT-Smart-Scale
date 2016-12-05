import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_newlogin
from src import myPasscode, myTextInput, myGenderSelection, myNumInput
import db_structure, db_access

class myUserSetup():
	def __init__(self, mainWindow):
		newUserInfo = db_structure.userDataStructure()
		self.widget = myGenderSelection.myGenderSelection(mainWindow, layoutSetting = "newUser_gender", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)

	def newUser_gender(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myGenderSelection.myGenderSelection(mainWindow, layoutSetting = "newUser_gender", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_email(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myTextInput.myTextInput(mainWindow, layoutSetting = "newUser_email", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_firstname(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myTextInput.myTextInput(mainWindow, layoutSetting = "newUser_firstname", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_lastname(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myTextInput.myTextInput(mainWindow, layoutSetting = "newUser_lastname", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_dob(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myNumInput.myNumInput(mainWindow, layoutSetting = "newUser_dob", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_height(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myNumInput.myNumInput(mainWindow, layoutSetting = "newUser_height", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_weight(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myNumInput.myNumInput(mainWindow, layoutSetting = "newUser_weight", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_passcode(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myPasscode.myPasscode(mainWindow, layoutSetting = "newUser_passcode", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_confirmPasscode(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myPasscode.myPasscode(mainWindow, layoutSetting = "newUser_confirmPasscode", dataStruc=newUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def newUser_add2db(self, mainWindow, newUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		if (db_access.user_register(newUserInfo)[0] == True):
			msg = QMessageBox.information(self, 'Success',"Account created",QMessageBox.Ok)
		else:
			msg = QMessageBox.information(self, 'Failed',"Server Error",QMessageBox.Ok)

	# def checkNewUserDetails(self,newUserInfo, option):
	# 	errorMsg = ""
	# 	if (option == "email"):
	# 		if (newUserInfo.email == ""): errorMsg = "Email can not be blank"
	# 		elif (" " in newUserInfo.email ): errorMsg = "Email can not contain Space"
	# 		elif ("@" not in newUserInfo.email ): errorMsg = "Invaild email format"
	# 		elif (db_access.user_checkIfEmailAlreadyRegisted(newUserInfo.email) == True): errorMsg = "This email address is already regsistered"
	# 	if (option == "firstname"):
	# 		if (newUserInfo.firstname == ""): errorMsg = "First name can not be blank"
	# 	if (option == "lastname"):
	# 		if (newUserInfo.lastname == ""): errorMsg = "Last name can not be blank"
	# 	if (option == "dob"):
	# 		if (newUserInfo.dob == ""): errorMsg = "Year of Birth can not be blank"
	# 	if (option == "height"):
	# 		if (newUserInfo.height == ""): errorMsg = "Height can not be blank"
	# 	if (option == "weight"):
	# 		if (newUserInfo.height == ""): errorMsg = "Weight can not be blank"
	# 	if (errorMsg != ""):
	# 		msg = QMessageBox.information(self, 'Error',errorMsg,QMessageBox.Ok)
	# 		return False
	# 	else: return True
