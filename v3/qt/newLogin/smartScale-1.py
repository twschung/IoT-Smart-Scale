import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_mainmenu, ui_loginmenu, ui_foodinformation, ui_scaleonly, ui_usersetup

import threading

class myMainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(myMainWindow, self).__init__(parent)
		self.setObjectName("mainWindow")
		self.resize(800, 480)
		self.central_widget = QStackedWidget()
		self.setCentralWidget(self.central_widget)
		self.widget = myMainMenu(self)
		self.central_widget.addWidget(self.widget)
		self.central_widget.setCurrentWidget(self.widget)

class myMainMenu(QWidget, ui_mainmenu.Ui_mainMenu):
	def __init__(self, mainWindow, name=None):
		super(myMainMenu, self).__init__()
		self.setupUi(self)
		self.btn_login.clicked.connect(lambda:self.handleBtn_login(mainWindow))
		self.btn_guest.clicked.connect(lambda:self.handleBtn_guest(mainWindow))
		self.btn_scaleOnly.clicked.connect(lambda:self.handleBtn_scaleOnly(mainWindow))
		self.btn_userSetup.clicked.connect(lambda:self.handleBtn_userSetup(mainWindow))
	def handleBtn_login(self, mainWindow):
		self.widget = myLoginMenu(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_guest(self, mainWindow):
		self.widget = myGuest(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_scaleOnly(self, mainWindow):
		self.widget = myScaleOnly(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_userSetup(self, mainWindow):
                something_clicked(self)
                self.widget = myUserSetup(mainWindow)
                mainWindow.central_widget.addWidget(self.widget)
                mainWindow.central_widget.setCurrentWidget(self.widget)

class myLoginMenu(QWidget, ui_loginmenu.Ui_loginMenu):
	def __init__(self, mainWindow, name=None):
		super(myLoginMenu, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_newLogin.clicked.connect(lambda:self.handleBtn_newLogin(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_newLogin(self, mainWindow):
		self.widget = myUserSetup(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)

class myGuest(QWidget, ui_foodinformation.Ui_foodInformation):
	def __init__(self, mainWindow, name=None):
		super(myGuest, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())

class myScaleOnly(QWidget, ui_scaleonly.Ui_scaleOnly):
	def __init__(self, mainWindow, name=None):
		super(myScaleOnly, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())

class myUserSetup(QWidget, ui_usersetup.Ui_userSetup):
	def __init__(self, mainWindow, name=None):
		super(myUserSetup, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())

class open_keyboard_thread (threading.Thread):
	def __init__(self):
		#print ("open_keyboard_thread init")
		threading.Thread.__init__(self)

	def run(self):
		#print ("open_keyboard_thread run")
		os.system("matchbox-keyboard")

def something_clicked(self):
	self.thread = open_keyboard_thread()
	self.thread.start()
	


 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = myMainWindow()
	window.showMaximized()
	sys.exit(app.exec_())
