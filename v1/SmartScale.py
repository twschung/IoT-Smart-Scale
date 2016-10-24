import sys, time, os

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import db_access, db_structure
import ftp_access
import numpy as np

import ui_login, ui_userRegister, ui_mainMenu, ui_userPasswordChange, ui_userDetailChange, ui_itemSuggestion

class loginWindow (QMainWindow, ui_login.Ui_login):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnLogin.clicked.connect(lambda:self.btnLogin_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
		self.btnExpressUser_1.clicked.connect(lambda:self.btnExpressUser_1_pressed())
		self.btnExpressUser_2.clicked.connect(lambda:self.btnExpressUser_2_pressed())
		self.btnExpressUser_3.clicked.connect(lambda:self.btnExpressUser_3_pressed())
		self.btnExpressUser_4.clicked.connect(lambda:self.btnExpressUser_4_pressed())
		self.btnExpressUser_5.clicked.connect(lambda:self.btnExpressUser_5_pressed())
		self.btnExpressUser_6.clicked.connect(lambda:self.btnExpressUser_6_pressed())
		self.processConfig()
	def btnLogin_pressed(self):
		loginResult = db_access.user_login(self.txtUsername.text(),self.txtPassword.text())
		if (loginResult[0] == False):
			self.lblStatus.setText ("ERROR: Incorrect Username or Password")
		else:
			self.lblStatus.setText ("Login Sccessful")
			self.currentUser = loginResult[1]
			if (self.chkExpressLogin.isChecked() == True):
				self.updateConfig()
			mainMenu(self)
		self.txtUsername.clear()
		self.txtPassword.clear()
	def btnRegister_pressed(self):
		userRegister(self)
	def btnExpressUser_1_pressed(self):
		self.expressLogin(self.config['expUsr_1'].username,self.config['expUsr_1'].password)
	def btnExpressUser_2_pressed(self):
		self.expressLogin(self.config['expUsr_2'].username,self.config['expUsr_2'].password)
	def btnExpressUser_3_pressed(self):
		self.expressLogin(self.config['expUsr_3'].username,self.config['expUsr_3'].password)
	def btnExpressUser_4_pressed(self):
		self.expressLogin(self.config['expUsr_4'].username,self.config['expUsr_4'].password)
	def btnExpressUser_5_pressed(self):
		self.expressLogin(self.config['expUsr_5'].username,self.config['expUsr_5'].password)
	def btnExpressUser_6_pressed(self):
		self.expressLogin(self.config['expUsr_6'].username,self.config['expUsr_6'].password)
	def expressLogin(self,username,password):
		loginResult = db_access.user_login(username,password)
		if (loginResult[0] == False):
			self.lblStatus.setText ("ERROR: Unknown Error")
		else:
			self.lblStatus.setText ("Login Sccessful")
			self.currentUser = loginResult[1]
			mainMenu(self)
	def processConfig(self):
		try:
			self.config = np.load('config.npy').item()
		except:
			blankSimpleUser = db_structure.simpleUserDataStructure()
			self.config = {'expUsr_1':blankSimpleUser , 'expUsr_2':blankSimpleUser , 'expUsr_3':blankSimpleUser , 'expUsr_4':blankSimpleUser , 'expUsr_5':blankSimpleUser , 'expUsr_6':blankSimpleUser}
			np.save('config.npy', self.config)
		finally:
			if (self.config['expUsr_1'].username != '~'):
				self.btnExpressUser_1.setEnabled(True)
				self.btnExpressUser_1.setText(("%s %s" % (self.config['expUsr_1'].firstname,self.config['expUsr_1'].lastname)))
			if (self.config['expUsr_2'].username != '~'):
				self.btnExpressUser_2.setEnabled(True)
				self.btnExpressUser_2.setText(("%s %s" % (self.config['expUsr_2'].firstname,self.config['expUsr_2'].lastname)))
			if (self.config['expUsr_3'].username != '~'):
				self.btnExpressUser_3.setEnabled(True)
				self.btnExpressUser_3.setText(("%s %s" % (self.config['expUsr_3'].firstname,self.config['expUsr_3'].lastname)))
			if (self.config['expUsr_4'].username != '~'):
				self.btnExpressUser_4.setEnabled(True)
				self.btnExpressUser_4.setText(("%s %s" % (self.config['expUsr_4'].firstname,self.config['expUsr_4'].lastname)))
			if (self.config['expUsr_5'].username != '~'):
				self.btnExpressUser_5.setEnabled(True)
				self.btnExpressUser_5.setText(("%s %s" % (self.config['expUsr_5'].firstname,self.config['expUsr_5'].lastname)))
			if (self.config['expUsr_6'].username != '~'):
				self.btnExpressUser_6.setEnabled(True)
				self.btnExpressUser_6.setText(("%s %s" % (self.config['expUsr_6'].firstname,self.config['expUsr_6'].lastname)))
	def updateConfig(self):
		if (self.currentUser.username != self.config['expUsr_1'].username and self.currentUser.username != self.config['expUsr_2'].username and self.currentUser.username != self.config['expUsr_3'].username and self.currentUser.username != self.config['expUsr_4'].username and self.currentUser.username != self.config['expUsr_5'].username and self.currentUser.username != self.config['expUsr_6'].username ):
			if (self.config['expUsr_1'].username == '~'):
				self.config['expUsr_1'] = self.updateExpUsr()
			elif (self.config['expUsr_2'].username == '~'):
				self.config['expUsr_2'] = self.updateExpUsr()
			elif (self.config['expUsr_3'].username == '~'):
				self.config['expUsr_3'] = self.updateExpUsr()
			elif (self.config['expUsr_4'].username == '~'):
				self.config['expUsr_4'] = self.updateExpUsr()
			elif (self.config['expUsr_5'].username == '~'):
				self.config['expUsr_5'] = self.updateExpUsr()
			elif (self.config['expUsr_6'].username == '~'):
				self.config['expUsr_6'] = self.updateExpUsr()
			np.save('config.npy', self.config)
	def updateExpUsr(self):
		expUsr = db_structure.simpleUserDataStructure()
		expUsr.username = self.currentUser.username
		expUsr.password = self.currentUser.password
		expUsr.firstname = self.currentUser.firstname
		expUsr.lastname = self.currentUser.lastname
		return expUsr
			
		
class userRegisterWindow (QMainWindow, ui_userRegister.Ui_userRegister):
	def __init__(self):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.btnCancel.clicked.connect(lambda:self.btnCancel_pressed())
		self.btnRegister.clicked.connect(lambda:self.btnRegister_pressed())
	def btnRegister_pressed(self):
		allFieldChecked = True
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
		self.pushButton_5.clicked.connect(lambda:self.pushButton_5_pressed())
	def btnChangePassword_pressed(self):
		userPasswordChange(self)
	def btnChangeUserDetail_pressed(self):
		userDetailChange(self)
	def btnLogout_pressed(self):
		login(self)
	def pushButton_5_pressed(self):
		itemSuggestion(self)
		
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
		self.txtEmail.setText(currentUser.email)
		self.txtFirstname.setText(currentUser.firstname)
		self.txtLastname.setText(currentUser.lastname)
		self.txtHeight.setText(currentUser.height)
		self.txtWeight.setText(currentUser.weight)
		if (currentUser.gender == "m"):
			self.rbnMale.setChecked(True)
			self.rbnFemale.setChecked(False)
		else:
			self.rbnMale.setChecked(False)
			self.rbnFemale.setChecked(True)
		self.datDoB.setDate(self.datDoB.date().fromString(currentUser.dob,"ddMMyyyy"))
		self.config = np.load('config.npy').item()
		if (self.currentUser.username == self.config['expUsr_1'].username or self.currentUser.username == self.config['expUsr_2'].username or self.currentUser.username == self.config['expUsr_3'].username or self.currentUser.username == self.config['expUsr_4'].username or self.currentUser.username == self.config['expUsr_5'].username or self.currentUser.username == self.config['expUsr_6'].username ):
			self.chkExpressLogin.setChecked(True)
		self.btnSubmitChanges.clicked.connect(lambda:self.btnSubmitChanges_pressed())
		self.btnCancel.clicked.connect(lambda:self.btnCancel_pressed())
	def btnSubmitChanges_pressed(self):
		allFieldChecked = True
		if (self.txtWeight.text().isdigit() == False or self.txtHeight.text().isdigit == False):
			allFieldChecked = False
			self.lblStatus.setText("ERROR : Please only enter numbers for Height and Weight")
		if (self.rbnMale.isChecked() == False and self.rbnFemale.isChecked() == False):
			allFieldChecked = False
			self.lblStatus.setText("ERROR : Gender not selected")
		if (self.txtEmail.text() == "" or self.txtFirstname.text() == "" or self.txtLastname.text() == "" or self.txtHeight.text() == "" or self.txtWeight.text() == ""):
			allFieldChecked = False
			self.lblStatus.setText("ERROR : Please fill in all fields")
		if (allFieldChecked == True):
			inputDoB = self.datDoB.date().toString('ddMMyyyy')
			inputGender = ""
			if (self.rbnMale.isChecked() == True): 
				inputGender = "m"
			if (self.rbnFemale.isChecked() == True): 
				inputGender = "f"
			updateUser = db_structure.userDataStructure(self.currentUser.id,self.currentUser.username,self.txtPassword.text(),self.txtEmail.text(),self.txtFirstname.text(),self.txtLastname.text(),inputDoB,inputGender,self.txtHeight.text(),self.txtWeight.text())
			dbResult = db_access.user_changeUserDetails(updateUser)
			if (dbResult[0] == False):
				if (dbResult[1] == 0): self.lblStatus.setText("ERROR : Incorrect Password")
				if (dbResult[1] == 1): self.lblStatus.setText("ERROR : DateBase error")
			if (dbResult[0] == True):
				self.currentUser = dbResult[1]
				self.updateConfig()
				mainMenu(self)
	def btnCancel_pressed(self):
		mainMenu(self)
	def updateConfig(self):
		if (self.chkExpressLogin.isChecked() == True):
			if (self.currentUser.username != self.config['expUsr_1'].username and self.currentUser.username != self.config['expUsr_2'].username and self.currentUser.username != self.config['expUsr_3'].username and self.currentUser.username != self.config['expUsr_4'].username and self.currentUser.username != self.config['expUsr_5'].username and self.currentUser.username != self.config['expUsr_6'].username ):
				if (self.config['expUsr_1'].username == '~'):
					self.config['expUsr_1'] = self.updateExpUsr()
				elif (self.config['expUsr_2'].username == '~'):
					self.config['expUsr_2'] = self.updateExpUsr()
				elif (self.config['expUsr_3'].username == '~'):
					self.config['expUsr_3'] = self.updateExpUsr()
				elif (self.config['expUsr_4'].username == '~'):
					self.config['expUsr_4'] = self.updateExpUsr()
				elif (self.config['expUsr_5'].username == '~'):
					self.config['expUsr_5'] = self.updateExpUsr()
				elif (self.config['expUsr_6'].username == '~'):
					self.config['expUsr_6'] = self.updateExpUsr()
		else:
			if (self.currentUser.username == self.config['expUsr_1'].username):
				self.config['expUsr_1'] = db_structure.simpleUserDataStructure()
			if (self.currentUser.username == self.config['expUsr_2'].username):
				self.config['expUsr_2'] = db_structure.simpleUserDataStructure()
			if (self.currentUser.username == self.config['expUsr_3'].username):
				self.config['expUsr_3'] = db_structure.simpleUserDataStructure()
			if (self.currentUser.username == self.config['expUsr_4'].username):
				self.config['expUsr_4'] = db_structure.simpleUserDataStructure()
			if (self.currentUser.username == self.config['expUsr_5'].username):
				self.config['expUsr_5'] = db_structure.simpleUserDataStructure()
			if (self.currentUser.username == self.config['expUsr_6'].username):
				self.config['expUsr_6'] = db_structure.simpleUserDataStructure()
		np.save('config.npy', self.config)
	def updateExpUsr(self):
		expUsr = db_structure.simpleUserDataStructure()
		expUsr.username = self.currentUser.username
		expUsr.password = self.currentUser.password
		expUsr.firstname = self.currentUser.firstname
		expUsr.lastname = self.currentUser.lastname
		return expUsr
		
class itemSuggestionWindow (QMainWindow, ui_itemSuggestion.Ui_itemSuggestion):
	def __init__(self, currentUser):
		super	(self.__class__, self).__init__()
		self.setupUi(self)
		self.currentUser = currentUser
		self.btnLogout.clicked.connect(lambda:self.btnLogout_pressed())
	def btnLogout_pressed(self):
		# tic = time.clock()
		# ftpSession = ftp_access.connectToServer()
		# ftp_access.downloadTempImage_1(ftpSession,"apple.jpg")
		# self.lblItem1.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_1(ftpSession,"banana.jpg")
		# self.lblItem2.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_1(ftpSession,"orange.jpg")
		# self.lblItem3.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_1(ftpSession,"mango.jpg")
		# self.lblItem4.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_1(ftpSession,"pear.jpg")
		# self.lblItem5.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.disconnectFromServer(ftpSession)
		# toc = time.clock()
		# print((toc - tic))
		# tic = time.clock()
		# ftp_access.downloadTempImage_2("apple.jpg")
		# self.lblItem5.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_2("banana.jpg")
		# self.lblItem4.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_2("orange.jpg")
		# self.lblItem3.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_2("mango.jpg")
		# self.lblItem2.setPixmap(QPixmap('temp.jpg'))
		# ftp_access.downloadTempImage_2("pear.jpg")
		# self.lblItem1.setPixmap(QPixmap('temp.jpg'))
		# toc = time.clock()
		# print((toc - tic))
		tic = time.clock()
		ftp_access.downloadTempImage_3("apple.jpg")
		self.lblItem5.setPixmap(QPixmap('temp.jpg'))
		ftp_access.downloadTempImage_3("banana.jpg")
		self.lblItem4.setPixmap(QPixmap('temp.jpg'))
		ftp_access.downloadTempImage_3("orange.jpg")
		self.lblItem3.setPixmap(QPixmap('temp.jpg'))
		ftp_access.downloadTempImage_3("mango.jpg")
		self.lblItem2.setPixmap(QPixmap('temp.jpg'))
		ftp_access.downloadTempImage_3("pear.jpg")
		self.lblItem1.setPixmap(QPixmap('temp.jpg'))
		toc = time.clock()
		print((toc - tic))
		
		
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
	
def itemSuggestion(self):
	self.close()
	currentForm = itemSuggestionWindow(self.currentUser)
	currentForm.show()
	
	

if __name__ == "__main__":
	main()