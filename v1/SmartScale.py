import sys

import PyQt5
from PyQt5.QtWidgets import *

import db_access

import ui_login
import ui_userRegister

class loginWindow (QMainWindow, ui_login.Ui_login):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnLogin.clicked.connect(lambda:self.btnLogin_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
	def btnLogin_pressed(self):
		self.loginResult = db_access.user_login(self.txtUsername.toPlainText(),self.txtPassword.toPlainText())
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
		print ("Button pressed")
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