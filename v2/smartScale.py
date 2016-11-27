import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_mainmenu, ui_loginmenu, ui_foodinformation, ui_scaleonly, ui_usersetup, ui_passcode
 
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
		self.btn_sub.clicked.connect(lambda:self.handleBtn_sub(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_sub(self, mainWindow):
		if(self.comboBox_passcode.currentText()=="Enabled" and self.comboBox_fingerprint.currentText()=="Enabled"):
			self.wt_passcode = myPasscode(mainWindow, self, option = 0)
			self.wt_passcode.lbl_title.setText("Set Passcode")
			self.wt_passcode.lbl_info.hide()
			self.wt_passcode.btn_forgot.hide()
			self.wt_passcode.show()
		elif(self.comboBox_passcode.currentText()=="Enabled"):
			self.wt_passcode = myPasscode(mainWindow, self, option = 1)
			self.wt_passcode.lbl_title.setText("Set Passcode")
			self.wt_passcode.lbl_info.hide()
			self.wt_passcode.btn_forgot.hide()
			self.wt_passcode.show()
		elif(self.comboBox_fingerprint.currentText()=="Enabled"):
			msg = QMessageBox.information(self, 'Fingerprint Login Setup',
				"Please place any of your finger/ thumb on the fingerprint scanner. You will need to use the same finger/ thumb for login.", 
				QMessageBox.Cancel | QMessageBox.Ok)
			if(msg == QMessageBox.Cancel):
				self.comboBox_fingerprint.setCurrentIndex(1)
			elif(msg == QMessageBox.Ok):
				msg = QMessageBox.information(self, 'Fingerprint Loging Setup',
				"Scanning fingerprint... Please wait.")
				mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())

class myPasscode(QWidget, ui_passcode.Ui_passCode):
	def __init__(self, mainWindow, userSetup, option, name=None):
		super(myPasscode, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow, userSetup, option))
		self.btn_done.clicked.connect(lambda:self.handleBtn_done(mainWindow, userSetup, option))
		self.btn_del.clicked.connect(lambda:self.handleBtn_del())
		self.btn_forgot.clicked.connect(lambda:self.handleBtn_forgot())
		nums = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine]
		for i in nums:
			i.clicked.connect(self.handleBtn_nums)
	def handleBtn_back(self, mainWindow, userSetup, option):
		if(option==0):
			userSetup.comboBox_passcode.setCurrentIndex(1)
			msg = QMessageBox.information(self, 'Fingerprint Login Setup',
				"Please place any of your finger/ thumb on the fingerprint scanner. You will need to use the same finger/ thumb for login.", 
				QMessageBox.Cancel | QMessageBox.Ok)
			if(msg == QMessageBox.Cancel):
				self.comboBox_fingerprint.setCurrentIndex(1)
			elif(msg == QMessageBox.Ok):
				msg = QMessageBox.information(self, 'Fingerprint Logging Setup',
				"Scanning fingerprint... Please wait.")
				mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
			self.close()
		elif(option==1):
			userSetup.comboBox_passcode.setCurrentIndex(1)
			self.close()
			mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_del(self):
		self.lineEdit_num.backspace()
	def handleBtn_done(self, mainWindow, userSetup, option):
		if(option==0):
			self.close()
			msg = QMessageBox.information(self, 'Fingerprint Login Setup',
				"Please place any of your finger/ thumb on the fingerprint scanner. You will need to use the same finger/ thumb for login.", 
				QMessageBox.Cancel | QMessageBox.Ok)
			if(msg == QMessageBox.Cancel):
				self.comboBox_fingerprint.setCurrentIndex(1)
			elif(msg == QMessageBox.Ok):
				msg = QMessageBox.information(self, 'Fingerprint Logging Setup',
				"Scanning fingerprint... Please wait.")
				mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		elif(option==1):
			self.close()
			mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		else:
			self.close()
	def handleBtn_nums(self):
		sender = self.sender()
		newNum = int(sender.text())
		setNum = str(newNum)
		self.lineEdit_num.setText(self.lineEdit_num.text() + setNum)
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = myMainWindow()
	window.show()
	sys.exit(app.exec_())