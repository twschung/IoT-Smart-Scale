import sys

import PyQt5
from PyQt5.QtWidgets import *

import db_access, db_structure

import ui_login
import ui_userRegister

class loginWindow (QMainWindow, ui_login.Ui_login):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnLogin.clicked.connect(lambda:self.btnLogin_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
	def btnLogin_pressed(self):
		self.loginResult = db_access.user_login(self.txtUsername.text(),self.txtPassword.text())
		if (self.loginResult[0] == False):
			self.lblStatus.setText ("Please enter Username and Password : (ERROR: Incorrect Username or Password)")
		else:
			self.loginResult[1].printUserDetails()
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
		if (self.txtPassword.text() != self.txtConfirmPassword.text()):
			allFieldChecked = False
			self.lblStatus.setText("Please enter the following details : (ERROR : Password does not match with confrim Passwrord)")
			self.txtPassword.clear()
			self.txtConfirmPassword.clear()
		if (self.rbnMale.isChecked() == False and self.rbnFemale.isChecked() == False):
			allFieldChecked = False
			self.lblStatus.setText("Please enter the following details : (ERROR : Gender not selected)")
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
				self.lblStatus.setText("Please enter the following details : (ERROR : Username is already used)")
				self.txtUsername.clear()
			if (dbResult[0] == True):
				login(self)
			
	def btnCancel_pressed(self):
		login(self)
	
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
	

if __name__ == "__main__":
	main()