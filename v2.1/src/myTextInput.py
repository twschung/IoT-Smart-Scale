import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_textInput
from src import myUserSetup, myUserLogin, myUserEdit, myCheckUserInfo

keyList=[\
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@','.',' '] , \
['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','.',' '] , \
['-','_',',','$','3','#','?','!','8','%','^','=','*','+','9','0','1','4','/','5','7','~','2','>','6','<','@','.',' '] ]

class myTextInput(QWidget, ui_textInput.Ui_textInput):
	def __init__(self, mainWindow, name=None, layoutSetting=None, dataStruc=None):
		super(myTextInput, self).__init__()
		self.setupUi(self)
		self.inputedText = str()
		self.shiftPressed = False
		self.numLockPressed = False
		self.updateKeyboardLayout()
		self.btnShift.clicked.connect(lambda:self.handle_btnShift())
		self.btnToggle.clicked.connect(lambda:self.handle_btnToggle())
		self.btnDel.clicked.connect(lambda:self.handle_btnDel())
		self.A.clicked.connect(lambda:self.handle_btn_key(0))
		self.B.clicked.connect(lambda:self.handle_btn_key(1))
		self.C.clicked.connect(lambda:self.handle_btn_key(2))
		self.D.clicked.connect(lambda:self.handle_btn_key(3))
		self.E.clicked.connect(lambda:self.handle_btn_key(4))
		self.F.clicked.connect(lambda:self.handle_btn_key(5))
		self.G.clicked.connect(lambda:self.handle_btn_key(6))
		self.H.clicked.connect(lambda:self.handle_btn_key(7))
		self.I.clicked.connect(lambda:self.handle_btn_key(8))
		self.J.clicked.connect(lambda:self.handle_btn_key(9))
		self.K.clicked.connect(lambda:self.handle_btn_key(10))
		self.L.clicked.connect(lambda:self.handle_btn_key(11))
		self.M.clicked.connect(lambda:self.handle_btn_key(12))
		self.N.clicked.connect(lambda:self.handle_btn_key(13))
		self.O.clicked.connect(lambda:self.handle_btn_key(14))
		self.P.clicked.connect(lambda:self.handle_btn_key(15))
		self.Q.clicked.connect(lambda:self.handle_btn_key(16))
		self.R.clicked.connect(lambda:self.handle_btn_key(17))
		self.S.clicked.connect(lambda:self.handle_btn_key(18))
		self.T.clicked.connect(lambda:self.handle_btn_key(19))
		self.U.clicked.connect(lambda:self.handle_btn_key(20))
		self.V.clicked.connect(lambda:self.handle_btn_key(21))
		self.W.clicked.connect(lambda:self.handle_btn_key(22))
		self.X.clicked.connect(lambda:self.handle_btn_key(23))
		self.Y.clicked.connect(lambda:self.handle_btn_key(24))
		self.Z.clicked.connect(lambda:self.handle_btn_key(25))
		self.btnAt.clicked.connect(lambda:self.handle_btn_key(26))
		self.btnDot.clicked.connect(lambda:self.handle_btn_key(27))
		self.space.clicked.connect(lambda:self.handle_btn_key(28))

		if (layoutSetting == "newUser_email"):
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Email: ")
			self.btn_login.setText("Next")
			self.btn_back.setText("Back")
			self.inputedText = dataStruc.email
			self.updateLineEdit()
			self.btn_login.clicked.connect(lambda:self.handle_btn_login_newUser_email(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_gender(self,mainWindow=mainWindow,newUserInfo=dataStruc))
		if (layoutSetting == "newUser_firstname"):
			self.btnAt.setEnabled(False)
			self.btnDot.setEnabled(False)
			self.btnToggle.setEnabled(False)
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Firstname: ")
			self.btn_login.setText("Next")
			self.btn_back.setText("Back")
			self.inputedText = dataStruc.firstname
			self.updateLineEdit()
			self.btn_login.clicked.connect(lambda:self.handle_btn_login_newUser_firstname(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_email(self,mainWindow=mainWindow,newUserInfo=dataStruc))
		if (layoutSetting == "newUser_lastname"):
			self.btnAt.setEnabled(False)
			self.btnDot.setEnabled(False)
			self.btnToggle.setEnabled(False)
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Lastname: ")
			self.btn_login.setText("Next")
			self.btn_back.setText("Back")
			self.inputedText = dataStruc.lastname
			self.updateLineEdit()
			self.btn_login.clicked.connect(lambda:self.handle_btn_login_newUser_lastname(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_firstname(self,mainWindow=mainWindow,newUserInfo=dataStruc))
		if (layoutSetting == "loginUser_email"):
			self.lbl_title.setText("User Login")
			self.lbl_currentText.setText("Email: ")
			self.btn_login.setText("Next")
			self.btn_back.setText("Back")
			self.inputedText = dataStruc.email
			self.updateLineEdit()
			self.btn_login.clicked.connect(lambda:self.handle_btn_login_loginUser_email(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
		if (layoutSetting == "editUser_firstname"):
			self.btnAt.setEnabled(False)
			self.btnDot.setEnabled(False)
			self.btnToggle.setEnabled(False)
			self.lbl_title.setText("Editing user details")
			self.lbl_currentText.setText("Firstname: ")
			self.btn_login.setText("Next")
			self.btn_back.setText("Back")
			self.inputedText = dataStruc.firstname
			self.updateLineEdit()
			self.btn_login.clicked.connect(lambda:self.handle_btn_login_editUser_firstname(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserEdit.myUserEdit.editUser_genderUser_email(self,mainWindow=mainWindow,currentUserInfo=dataStruc))
		if (layoutSetting == "editUser_lastname"):
			self.btnAt.setEnabled(False)
			self.btnDot.setEnabled(False)
			self.btnToggle.setEnabled(False)
			self.lbl_title.setText("Editing user details")
			self.lbl_currentText.setText("Lastname: ")
			self.btn_login.setText("Next")
			self.btn_back.setText("Back")
			self.inputedText = dataStruc.lastname
			self.updateLineEdit()
			self.btn_login.clicked.connect(lambda:self.handle_btn_login_editUser_lastname(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserEdit.myUserEdit.editUser_firstname(self,mainWindow=mainWindow,currentUserInfo=dataStruc))

	def handle_btn_login_newUser_email(self, mainWindow, dataStruc):
		dataStruc.email=self.inputedText
		dataStruc.username=self.inputedText
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "email")==True):
			myUserSetup.myUserSetup.newUser_firstname(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handle_btn_login_newUser_firstname(self, mainWindow, dataStruc):
		dataStruc.firstname=self.inputedText
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "firstname")==True):
			myUserSetup.myUserSetup.newUser_lastname(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handle_btn_login_newUser_lastname(self, mainWindow, dataStruc):
		dataStruc.lastname=self.inputedText
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "lastname")==True):
			myUserSetup.myUserSetup.newUser_dob(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handle_btn_login_loginUser_email(self, mainWindow, dataStruc):
		dataStruc.email=self.inputedText
		dataStruc.username=self.inputedText
		myUserLogin.myUserLogin.loginUser_passcode(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
	def handle_btn_login_editUser_firstname(self, mainWindow, dataStruc):
		dataStruc.firstname=self.inputedText
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "firstname")==True):
			myUserEdit.myUserEdit.editUser_lastname(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
	def handle_btn_login_editUser_lastname(self, mainWindow, dataStruc):
		dataStruc.lastname=self.inputedText
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "lastname")==True):
			myUserEdit.myUserEdit.editUser_dob(self,mainWindow=mainWindow,currentUserInfo=dataStruc)

	def updateKeyboardLayout(self):
		keyset = 0
		if (self.shiftPressed == True): keyset = 1
		if (self.numLockPressed == True): keyset = 2
		self.A.setText(keyList[keyset][0])
		self.B.setText(keyList[keyset][1])
		self.C.setText(keyList[keyset][2])
		self.D.setText(keyList[keyset][3])
		self.E.setText(keyList[keyset][4])
		self.F.setText(keyList[keyset][5])
		self.G.setText(keyList[keyset][6])
		self.H.setText(keyList[keyset][7])
		self.I.setText(keyList[keyset][8])
		self.J.setText(keyList[keyset][9])
		self.K.setText(keyList[keyset][10])
		self.L.setText(keyList[keyset][11])
		self.M.setText(keyList[keyset][12])
		self.N.setText(keyList[keyset][13])
		self.O.setText(keyList[keyset][14])
		self.P.setText(keyList[keyset][15])
		self.Q.setText(keyList[keyset][16])
		self.R.setText(keyList[keyset][17])
		self.S.setText(keyList[keyset][18])
		self.T.setText(keyList[keyset][19])
		self.U.setText(keyList[keyset][20])
		self.V.setText(keyList[keyset][21])
		self.W.setText(keyList[keyset][22])
		self.X.setText(keyList[keyset][23])
		self.Y.setText(keyList[keyset][24])
		self.Z.setText(keyList[keyset][25])
	def updateLineEdit(self):
		self.lineEdit_currentText.setText(self.inputedText)
	def handle_btnDel(self):
		self.inputedText = self.inputedText[:(len(self.inputedText)-1)]
		self.updateLineEdit()
	def handle_btn_key(self, charNum):
		if (self.shiftPressed == True):
			charPressed = keyList[1][charNum]
			self.shiftPressed = False
			self.updateKeyboardLayout()
		elif (self.numLockPressed == True):
			charPressed = keyList[2][charNum]
		else :
			charPressed = keyList[0][charNum]
		self.inputedText += charPressed
		self.updateLineEdit()
	def handle_btnShift(self):
		if (self.shiftPressed == False):
			self.shiftPressed = True
			self.numLockPressed = False
		else:
			self.shiftPressed = False
		self.updateKeyboardLayout()
	def handle_btnToggle(self):
		if (self.numLockPressed == False):
			self.numLockPressed = True
			self.shiftPressed = False
		else:
			self.numLockPressed = False
		self.updateKeyboardLayout()
	def numOnlyMode(self):
		self.numLockPressed = True
		self.btnToggle.setEnabled(False)
		self.btnShift.setEnabled(False)
		self.updateKeyboardLayout()
		self.A.setEnabled(False)
		self.S.setEnabled(False)
		self.D.setEnabled(False)
		self.F.setEnabled(False)
		self.G.setEnabled(False)
		self.H.setEnabled(False)
		self.J.setEnabled(False)
		self.K.setEnabled(False)
		self.L.setEnabled(False)
		self.Z.setEnabled(False)
		self.X.setEnabled(False)
		self.C.setEnabled(False)
		self.V.setEnabled(False)
		self.B.setEnabled(False)
		self.N.setEnabled(False)
		self.M.setEnabled(False)
		self.space.setEnabled(False)
		self.btnAt.setEnabled(False)
