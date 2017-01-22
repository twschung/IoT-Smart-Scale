import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_passcode
import myUserSetup, myLoginMenu, myUserEdit, myUserLogin, myForgotPasscode, myPasscodeMenu
import db_access

class myPasscode(QWidget, ui_passcode.Ui_passCode):
	def __init__(self, mainWindow, name=None, layoutSetting=None, dataStruc=None, newUser=False):
		super(myPasscode, self).__init__()
		self.setupUi(self)
		self.passcode = str()
		self.btn_del.clicked.connect(lambda:self.handleBtn_del())
		self.btn_0.clicked.connect(lambda:self.handleBtn_0())
		self.btn_1.clicked.connect(lambda:self.handleBtn_1())
		self.btn_2.clicked.connect(lambda:self.handleBtn_2())
		self.btn_3.clicked.connect(lambda:self.handleBtn_3())
		self.btn_4.clicked.connect(lambda:self.handleBtn_4())
		self.btn_5.clicked.connect(lambda:self.handleBtn_5())
		self.btn_6.clicked.connect(lambda:self.handleBtn_6())
		self.btn_7.clicked.connect(lambda:self.handleBtn_7())
		self.btn_8.clicked.connect(lambda:self.handleBtn_8())
		self.btn_9.clicked.connect(lambda:self.handleBtn_9())
		self.btn_done.setEnabled(False)
		self.btn_del.setEnabled(False)
		self.btn_remUser.setVisible(False)
		self.btn_remFingerPrint.setVisible(False)
		if (layoutSetting == "newUser_passcode"):
			self.btn_forgot.setVisible(False)
			self.lbl_title.setText("New User Setup Wizard ")
			self.lbl_info.setText("Please Enter a New Passcode")
			self.btn_done.setText("Next")
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_newPasscode(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_weight(self,mainWindow=mainWindow,newUserInfo=dataStruc))
		if (layoutSetting == "newUser_confirmPasscode"):
			self.btn_forgot.setVisible(False)
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_info.setText("Please confirm New Passcode")
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_newConfirmPasscode(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_passcode(self,mainWindow=mainWindow,newUserInfo=dataStruc))
		if (layoutSetting == "loginUser_passcode"):
			self.lbl_title.setText("User login")
			self.lbl_info.setText("Please enter Passcode")
			self.btn_remUser.setVisible(True)
			# self.btn_remFingerPrint.setVisible(True)
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_loginPasscode(mainWindow,dataStruc))
			if(newUser==True):
				self.btn_back.clicked.connect(lambda:myUserLogin.myUserLogin.loginUser_email(self,mainWindow=mainWindow,currentUserInfo=dataStruc))
			else:
				self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
			self.btn_forgot.clicked.connect(lambda:self.handleBtn_forgot(mainWindow,dataStruc))
			if(myUserLogin.myUserLogin.checkRemeberUserStatus(self,dataStruc) == True):
				self.btn_remUser.setText("Forget User")
				self.btn_remUser.clicked.connect(lambda:self.handleBtn_forgetUser(mainWindow,dataStruc))
			else:
				self.btn_remUser.clicked.connect(lambda:self.handleBtn_remUser())
		if (layoutSetting == "editUser_verifyPasscode"):
			self.btn_forgot.setVisible(False)
			self.lbl_title.setText("Passcode Verification")
			self.lbl_info.setText("Please Enter Passcode")
			self.btn_done.setText("Next")
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_editUser_verfyPasscode(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
		if (layoutSetting == "editUser_oldPasscode"):
			self.btn_forgot.setVisible(False)
			self.btn_remUser.setVisible(False)
			if (myUserLogin.myUserLogin.checkRemeberUserStatus(self, currentUserInfo=dataStruc) == True):
				self.btn_remUser.setChecked(True)
			else:
				self.btn_remUser.setChecked(False)
			self.lbl_title.setText("Passcode Verification")
			self.lbl_info.setText("Please Enter Passcode")
			self.btn_done.setText("Next")
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_editUser_oldPasscode(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:self.handleBtn_back_editUser_oldPasscode(mainWindow,dataStruc))
		if (layoutSetting == "editUser_newPasscode"):
			self.btn_forgot.setVisible(False)
			self.lbl_title.setText("Changing Passcode")
			self.lbl_info.setText("Please Enter New Passcode")
			self.btn_done.setText("Next")
			self.btn_back.setEnabled(False)
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_editUser_newPasscode(mainWindow,dataStruc))
		if (layoutSetting == "editUser_confirmPasscode"):
			self.btn_forgot.setVisible(False)
			self.lbl_title.setText("Changing Passcode")
			self.lbl_info.setText("Please Confirm New Passcode")
			self.btn_done.setText("Submit")
			self.btn_back.clicked.connect(lambda:myUserEdit.myUserEdit.editUser_newPasscode(self,mainWindow=mainWindow,currentUserInfo=dataStruc))
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_editUser_confirmPasscode(mainWindow,dataStruc))
	def handleBtn_back(self,mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		self.widget = myLoginMenu.myLoginMenu(mainWindow)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_done_newPasscode(self, mainWindow, dataStruc):
		dataStruc.password = self.passcode
		myUserSetup.myUserSetup.newUser_confirmPasscode(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handleBtn_done_newConfirmPasscode(self, mainWindow, dataStruc):
		if (dataStruc.password == self.passcode):
			myUserSetup.myUserSetup.newUser_add2db(self,mainWindow=mainWindow,newUserInfo=dataStruc)
		else:
			msg = QMessageBox.information(self, 'Error',"Passcode doesnt not match",QMessageBox.Ok)
			dataStruc.passcode = ""
			myUserSetup.myUserSetup.newUser_passcode(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handleBtn_done_loginPasscode(self, mainWindow, dataStruc):
		dataStruc.password = self.passcode
		db_result = db_access.user_login(dataStruc.username,dataStruc.password)
		if (db_result[0] == True):
			currentUserInfo = db_result[1]
			if (self.btn_remUser.isChecked()==True and self.btn_remFingerPrint.isChecked()==True):
				myUserLogin.myUserLogin.rememberUserAndFingerPrint(self,currentUserInfo)
			elif (self.btn_remUser.isChecked()==True and self.btn_remFingerPrint.isChecked()==False):
				myUserLogin.myUserLogin.rememberUser(self,currentUserInfo)
			myUserLogin.myUserLogin.enterUserMenu(self,mainWindow=mainWindow,currentUserInfo=currentUserInfo)
		else:
			msg = QMessageBox.information(self, 'Failed',"Email / Passcode Incorrect",QMessageBox.Ok)
	def handleBtn_done_editUser_verfyPasscode(self, mainWindow, dataStruc):
		if (self.passcode == dataStruc.password):
			myUserEdit.myUserEdit.editUser_gender(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
		else:
			msg = QMessageBox.information(self, 'Failed',"Passcode Incorrect",QMessageBox.Ok)
	def handleBtn_done_editUser_oldPasscode(self, mainWindow, dataStruc):
		if (self.passcode == dataStruc.password):
			self.widget = myPasscodeMenu.myPasscodeMenu(mainWindow=mainWindow,currentUserInfo=dataStruc)
			mainWindow.central_widget.addWidget(self.widget)
			mainWindow.central_widget.setCurrentWidget(self.widget)
			if (self.btn_remUser.isChecked() == True):
				myUserLogin.myUserLogin.rememberUser(self, currentUserInfo=dataStruc)
			else:
				myUserLogin.myUserLogin.forgetUser(self, currentUserInfo=dataStruc)
		else:
			msg = QMessageBox.information(self, 'Failed',"Passcode Incorrect",QMessageBox.Ok)
	def handleBtn_done_editUser_newPasscode(self, mainWindow, dataStruc):
		dataStruc.password = self.passcode
		myUserEdit.myUserEdit.editUser_confirmPasscode(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
	def handleBtn_done_editUser_confirmPasscode(self, mainWindow, dataStruc):
		if (dataStruc.password == self.passcode):
			myUserEdit.myUserEdit.editUserPasscodes_add2db(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
		else:
			msg = QMessageBox.information(self, 'Error',"Passcode doesnt not match",QMessageBox.Ok)
			dataStruc.passcode = ""
			myUserEdit.myUserEdit.editUser_newPasscode(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
	def handleBtn_back_editUser_oldPasscode(self, mainWindow, dataStruc):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	'''
		if (self.btn_remUser.isChecked() == True):
			myUserLogin.myUserLogin.rememberUser(self, currentUserInfo=dataStruc)
		else:
			myUserLogin.myUserLogin.forgetUser(self, currentUserInfo=dataStruc)
	'''
	def handleBtn_forgetUser(self,mainWindow,dataStruc):
		myUserLogin.myUserLogin.forgetUser(self,dataStruc)
		msg = QMessageBox.information(self, 'Forgotten',"You have been removed from the login menu.",QMessageBox.Ok)
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_remUser(self):
		if (self.btn_remUser.isChecked()== True):
			self.btn_remFingerPrint.setEnabled(True)
		else:
			self.btn_remFingerPrint.setEnabled(False)
			self.btn_remFingerPrint.setChecked(False)
	def handleBtn_forgot(self,mainWindow,currentUserInfo):
		self.widget = myForgotPasscode.myForgotPasscode(mainWindow=mainWindow,currentUserInfo=currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)

	def updateLineEdit(self):
		self.btn_done.setEnabled(False)
		self.btn_del.setEnabled(True)
		self.btn_0.setEnabled(True)
		self.btn_1.setEnabled(True)
		self.btn_2.setEnabled(True)
		self.btn_3.setEnabled(True)
		self.btn_4.setEnabled(True)
		self.btn_5.setEnabled(True)
		self.btn_6.setEnabled(True)
		self.btn_7.setEnabled(True)
		self.btn_8.setEnabled(True)
		self.btn_9.setEnabled(True)
		if (len(self.passcode) == 0):
			self.lineEdit_1.setText("")
			self.lineEdit_2.setText("")
			self.lineEdit_3.setText("")
			self.lineEdit_4.setText("")
			self.btn_del.setEnabled(False)
		elif (len(self.passcode) == 1):
			self.lineEdit_1.setText("X")
			self.lineEdit_2.setText("")
			self.lineEdit_3.setText("")
			self.lineEdit_4.setText("")
		elif (len(self.passcode) == 2):
			self.lineEdit_1.setText("X")
			self.lineEdit_2.setText("X")
			self.lineEdit_3.setText("")
			self.lineEdit_4.setText("")
		elif (len(self.passcode) == 3):
			self.lineEdit_1.setText("X")
			self.lineEdit_2.setText("X")
			self.lineEdit_3.setText("X")
			self.lineEdit_4.setText("")
		elif (len(self.passcode) == 4):
			self.lineEdit_1.setText("X")
			self.lineEdit_2.setText("X")
			self.lineEdit_3.setText("X")
			self.lineEdit_4.setText("X")
			self.btn_0.setEnabled(False)
			self.btn_1.setEnabled(False)
			self.btn_2.setEnabled(False)
			self.btn_3.setEnabled(False)
			self.btn_4.setEnabled(False)
			self.btn_5.setEnabled(False)
			self.btn_6.setEnabled(False)
			self.btn_7.setEnabled(False)
			self.btn_8.setEnabled(False)
			self.btn_9.setEnabled(False)
			self.btn_done.setEnabled(True)
	def addNum2Passcode(self, num):
		if (len(self.passcode)<4):
			self.passcode += num
			self.updateLineEdit()
	def handleBtn_del(self):
		if(len(self.passcode)>0):
			self.passcode = self.passcode[:(len(self.passcode)-1)]
			self.updateLineEdit()
	def handleBtn_0(self): self.addNum2Passcode('0')
	def handleBtn_1(self): self.addNum2Passcode('1')
	def handleBtn_2(self): self.addNum2Passcode('2')
	def handleBtn_3(self): self.addNum2Passcode('3')
	def handleBtn_4(self): self.addNum2Passcode('4')
	def handleBtn_5(self): self.addNum2Passcode('5')
	def handleBtn_6(self): self.addNum2Passcode('6')
	def handleBtn_7(self): self.addNum2Passcode('7')
	def handleBtn_8(self): self.addNum2Passcode('8')
	def handleBtn_9(self): self.addNum2Passcode('9')
