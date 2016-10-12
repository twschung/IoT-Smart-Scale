import sys

import PyQt5
from PyQt5.QtWidgets import *

import ui_userRegister

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
	form = userRegisterWindow()
	form.show()
	sys.exit(app.exec_())
	
if __name__ == "__main__":
	main()