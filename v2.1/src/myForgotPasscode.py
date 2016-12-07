import sys
sys.path.insert(0,"/home/pi/Desktop/v2.1/src")
sys.path.insert(0,"/home/pi/Desktop/v2.1/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import myScaleOnly
import ui_forgotpasscode

class myForgotPasscode(QWidget, ui_forgotpasscode.Ui_forgotPasscode):
	def __init__(self, mainWindow, currentUserInfo, name=None, layoutSetting=None):
		super(myForgotPasscode, self).__init__()
		self.setupUi(self)
		self.btn_back.setText("Back")
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_guest.clicked.connect(lambda:self.handleBtn_guest(mainWindow))
		self.btn_send.clicked.connect(lambda:self.handleBtn_send(mainWindow,currentUserInfo))
	def handleBtn_back(self,mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_guest(self,mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myScaleOnly.myScaleOnly(mainWindow)
		self.widget.btn_back.setText("Main Menu")
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_send(self,mainWindow,currentUserInfo):
		msg = QMessageBox.information(self, 'Sent',"Passcode has been sent to " + currentUserInfo.username,QMessageBox.Ok)
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())


