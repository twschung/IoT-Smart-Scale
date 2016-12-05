import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_newlogin
from src import myPasscode, myTextInput, myGenderSelection, myNumInput, myUserLogin
import db_structure, db_access

class myUserEdit():
	def editUser_verifyPasscode(self,mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myPasscode.myPasscode(mainWindow, layoutSetting = "editUser_verifyPasscode", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_gender(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myGenderSelection.myGenderSelection(mainWindow, layoutSetting = "editUser_gender", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_firstname(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myTextInput.myTextInput(mainWindow, layoutSetting = "editUser_firstname", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_lastname(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myTextInput.myTextInput(mainWindow, layoutSetting = "editUser_lastname", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_dob(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myNumInput.myNumInput(mainWindow, layoutSetting = "editUser_dob", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_height(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myNumInput.myNumInput(mainWindow, layoutSetting = "editUser_height", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_weight(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myNumInput.myNumInput(mainWindow, layoutSetting = "editUser_weight", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_add2db(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		if (db_access.user_changeUserDetails(currentUserInfo)[0] == True):
			msg = QMessageBox.information(self, 'Success',"Saved Changes",QMessageBox.Ok)
			mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
			mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
			myUserLogin.myUserLogin.enterUserMenu(self, mainWindow, currentUserInfo)
		else:
			msg = QMessageBox.information(self, 'Failed',"Server Error",QMessageBox.Ok)

	def editUser_oldPasscode(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myPasscode.myPasscode(mainWindow, layoutSetting = "editUser_oldPasscode", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_newPasscode(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myPasscode.myPasscode(mainWindow, layoutSetting = "editUser_newPasscode", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUser_confirmPasscode(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myPasscode.myPasscode(mainWindow, layoutSetting = "editUser_confirmPasscode", dataStruc=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def editUserPasscodes_add2db(self, mainWindow, currentUserInfo):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		if (db_access.user_changePassword(currentUserInfo)[0] == True):
			msg = QMessageBox.information(self, 'Success',"Saved Changes",QMessageBox.Ok)
			mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
			mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
			myUserLogin.myUserLogin.enterUserMenu(self, mainWindow, currentUserInfo)
		else:
			msg = QMessageBox.information(self, 'Failed',"Server Error",QMessageBox.Ok)

	# def checkUserDetails(self,currentUserInfo, option):
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
