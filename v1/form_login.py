import sys

import PyQt5
from PyQt5.QtWidgets import *

import ui_login
import ui_userRegister

class LoginWindow (QMainWindow, ui_login.Ui_login):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnLogin.clicked.connect(lambda:self.btnLogin_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
	def btnLogin_pressed(self):
		print (self.txtUsername.toPlainText())
		print (self.txtPassword.toPlainText())
		self.txtPassword.clear()
	def btnRegister_pressed(self):
		print ("Button pressed")
		userRegister()
		
class userRegisterWindow (QMainWindow, ui_userRegister.Ui_userRegister):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnCancel.clicked.connect(lambda:self.btnCancel_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
	def btnRegister_pressed(self):
		print ("Button pressed")
	def btnCancel_pressed(self):
		print ("Button pressed")
	
def main():
	app = QApplication(sys.argv)
	form = LoginWindow()
	form.show()
	sys.exit(app.exec_())
	
def userRegister():
	form = userRegisterWindow()
	form.show()
	
	

	
if __name__ == "__main__":
	main()