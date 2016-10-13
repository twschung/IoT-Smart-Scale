import sys

import PyQt5
from PyQt5.QtWidgets import *

import db_access, db_structure

import ui_login, ui_userRegister, ui_mainMenu, ui_userPasswordChange, ui_userDetailChange

class loginWindow (QMainWindow, ui_login.Ui_login):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnLogin.clicked.connect(lambda:self.btnLogin_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
	def btnLogin_pressed(self):
		loginResult = db_access.user_login(self.txtUsername.text(),self.txtPassword.text())
		if (loginResult[0] == False):
			self.lblStatus.setText ("ERROR: Incorrect Username or Password")
		else:
			self.lblStatus.setText ("Login Sccessful")
			self.currentUser = loginResult[1]
			mainMenu(self)
		self.txtUsername.clear()
		self.txtPassword.clear()
	def btnRegister_pressed(self):
		userRegister(self)
		
class userRegisterWindow (QMainWindow, ui_userRegister.Ui_userRegister):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnCancel.clicked.connect(lambda:self.btnCancel_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
	def btnRegister_pressed(self):
		allFieldChecked = True
		# XH please add more error catching for input parameters here
		if (self.txtWeight.text().isdigit() == False or self.txtHeight.text().isdigit == False):
			allFieldChecked = False
			self.lblStatus.setText("ERROR : Please only enter numbers for Height and Weight")
		if (self.rbnMale.isChecked() == False and self.rbnFemale.isChecked() == False):
			allFieldChecked = False
			self.lblStatus.setText("ERROR : Gender not selected")
		if (self.txtUsername.text() == "" or self.txtPassword.text() == "" or self.txtEmail.text() == "" or self.txtFirstname.text() == "" or self.txtLastname.text() == "" or self.txtHeight.text() == "" or self.txtWeight.text() == ""):
			allFieldChecked = False
			self.lblStatus.setText("ERROR : Please fill in all fields")
		if (self.txtPassword.text() != self.txtConfirmPassword.text()):
			allFieldChecked = False
			self.lblStatus.setText("ERROR : Password does not match with confrim Password")
			self.txtPassword.clear()
			self.txtConfirmPassword.clear()
		if (allFieldChecked == True):
			inputDoB = self.datDoB.date().toString('ddMMyyyy')
			inputGender = ""
			if (self.rbnMale.isChecked() == True): 
				inputGender = "m"
			if (self.rbnFemale.isChecked() == True): 
				inputGender = "f"
			newUser = db_structure.userDataStructure("0", self.txtUsername.text(), self.txtPassword.text(), self.txtEmail.text(), self.txtFirstname.text(), self.txtLastname.text(), inputDoB, inputGender, self.txtHeight.text(), self.txtWeight.text())
			dbResult = db_access.user_register(newUser)
			if (dbResult[0] == False):
				self.lblStatus.setText("ERROR : Username is already used")
				self.txtUsername.clear()
			if (dbResult[0] == True):
				login(self)
	def btnCancel_pressed(self):
		login(self)
	
class mainMenuWindow (QMainWindow, ui_mainMenu.Ui_mainMenu):
	def __init__(self, currentUser):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.currentUser = currentUser
		self.lblStatus.setText(("Hi! Welcome back! %s %s" % (self.currentUser.firstname, self.currentUser.lastname)))
		self.btnLogout.clicked.connect(lambda:self.btnLogout_pressed())
		self.btnChangePassword.clicked.connect(lambda:self.btnChangePassword_pressed())
		self.btnChangeUserDetail.clicked.connect(lambda:self.btnChangeUserDetail_pressed())
	def btnChangePassword_pressed(self):
		userPasswordChange(self)
	def btnChangeUserDetail_pressed(self):
		userDetailChange(self)
	def btnLogout_pressed(self):
		login(self)
		
class userPasswordChangeWindow (QMainWindow, ui_userPasswordChange.Ui_userPasswordChange):
	def __init__(self, currentUser):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.currentUser = currentUser
		self.btnChangePassword.clicked.connect(lambda:self.btnChangePassword_pressed())
		self.btnCancel.clicked.connect(lambda:self.btnCancel_pressed())
	def btnChangePassword_pressed(self):
		allFieldChecked = True
		if (self.txtNewPassword.text() != self.txtConfirmPassword.text()):
			allFieldChecked = False
			self.lblStatus.setText("Error : Comfirm Password does not match with New Password")
			self.txtNewPassword.clear()
			self.txtConfirmPassword.clear()
		if (self.txtNewPassword.text() == ""):
			allFieldChecked = False
			self.lblStatus.setText("Error : Can not have a blank password")
		if (allFieldChecked ==  True):
			dbResult = db_access.user_changePassword(self.currentUser, self.txtOldPassword.text(), self.txtNewPassword.text())
			if (dbResult[0] == True):
				self.currentUser = dbResult[1]
				mainMenu(self)
			else:
				if (dbResult[1] == 0):
					self.lblStatus.setText("Error : Old Password is incorrect")
					self.txtOldPassword.clear()
				if (dbResult[1] == 1):
					self.lblStatus.setText("Error : DataBase Error")
	def btnCancel_pressed(self):
		mainMenu(self)
		
class userDetailChangeWindow (QMainWindow, ui_userDetailChange.Ui_userDetailChange):
	def __init__(self, currentUser):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.currentUser = currentUser
		
		self.btnCancel.clicked.connect(lambda:self.btnCancel_pressed())
	def btnCancel_pressed(self):
		mainMenu(self)
		

def main():
	app = QApplication(sys.argv)
	currentForm = loginWindow()
	currentForm.show()
	sys.exit(app.exec_())
	
def login(self):
	self.close()
	currentForm = loginWindow()
	currentForm.show()
	
def userRegister(self):
	self.close()
	currentForm = userRegisterWindow()
	currentForm.show()
	
def mainMenu(self):
	self.close()
	currentForm = mainMenuWindow(self.currentUser)
	currentForm.show()

def userPasswordChange(self):
	self.close()
	currentForm = userPasswordChangeWindow(self.currentUser)
	currentForm.show()
	
def userDetailChange(self):
	self.close()
	currentForm = userDetailChangeWindow(self.currentUser)
	currentForm.show()
	

if __name__ == "__main__":
	main()