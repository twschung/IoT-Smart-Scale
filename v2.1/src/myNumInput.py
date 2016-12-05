import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_numInput
from src import myUserSetup, myUserEdit, myCheckUserInfo

class myNumInput(QWidget, ui_numInput.Ui_numInput):
	def __init__(self, mainWindow, name=None, layoutSetting=None, dataStruc=None):
		super(myNumInput, self).__init__()
		self.setupUi(self)
		self.inputedText = str()
		self.decimalEnable = False
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
		self.btn_dot.clicked.connect(lambda:self.handleBtn_dot())
		if (layoutSetting == "newUser_dob"):
			self.inputedText = dataStruc.dob
			self.updateLineEdit()
			self.btn_dot.setEnabled(False)
			self.btn_unit.setEnabled(False)
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Year of Birth: ")
			self.btn_next.clicked.connect(lambda:self.handleBtn_next_newDob(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_lastname(self,mainWindow=mainWindow,newUserInfo=dataStruc))
		if (layoutSetting == "newUser_height"):
			self.inputedText = dataStruc.height
			self.updateLineEdit()
			self.decimalEnable = True
			self.btn_dot.setEnabled(True)
			self.btn_unit.setEnabled(True)
			self.btn_unit.setText("Meter")
			self.unit = "m"
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Height: ")
			self.btn_next.clicked.connect(lambda:self.handleBtn_next_newHeight(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_dob(self,mainWindow=mainWindow,newUserInfo=dataStruc))
			self.btn_unit.clicked.connect(lambda:self.handle_btn_unit_height())
		if (layoutSetting == "newUser_weight"):
			self.inputedText = dataStruc.weight
			self.updateLineEdit()
			self.decimalEnable = True
			self.btn_dot.setEnabled(True)
			self.btn_unit.setEnabled(True)
			self.btn_unit.setText("kg")
			self.unit = "k"
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Weight: ")
			self.btn_next.clicked.connect(lambda:self.handleBtn_next_newWeight(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserSetup.myUserSetup.newUser_height(self,mainWindow=mainWindow,newUserInfo=dataStruc))
			self.btn_unit.clicked.connect(lambda:self.handle_btn_unit_weight())
		if (layoutSetting == "editUser_dob"):
			self.inputedText = dataStruc.dob
			self.updateLineEdit()
			self.btn_dot.setEnabled(False)
			self.btn_unit.setEnabled(False)
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Year of Birth: ")
			self.btn_next.clicked.connect(lambda:self.handleBtn_next_editDob(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserEdit.myUserEdit.editUser_lastname(self,mainWindow=mainWindow,currentUserInfo=dataStruc))
		if (layoutSetting == "editUser_height"):
			self.inputedText = dataStruc.height
			self.updateLineEdit()
			self.decimalEnable = True
			self.btn_dot.setEnabled(True)
			self.btn_unit.setEnabled(True)
			self.btn_unit.setText("Meter")
			self.unit = "m"
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Height: ")
			self.btn_next.clicked.connect(lambda:self.handleBtn_next_editHeight(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserEdit.myUserEdit.editUser_dob(self,mainWindow=mainWindow,currentUserInfo=dataStruc))
			self.btn_unit.clicked.connect(lambda:self.handle_btn_unit_height())
		if (layoutSetting == "editUser_weight"):
			self.inputedText = dataStruc.weight
			self.updateLineEdit()
			self.decimalEnable = True
			self.btn_dot.setEnabled(True)
			self.btn_unit.setEnabled(True)
			self.btn_unit.setText("kg")
			self.btn_next.setText("Done")
			self.unit = "k"
			self.lbl_title.setText("New User Setup Wizard")
			self.lbl_currentText.setText("Weight: ")
			self.btn_next.clicked.connect(lambda:self.handleBtn_next_editWeight(mainWindow,dataStruc))
			self.btn_back.clicked.connect(lambda:myUserEdit.myUserEdit.editUser_height(self,mainWindow=mainWindow,currentUserInfo=dataStruc))
			self.btn_unit.clicked.connect(lambda:self.handle_btn_unit_weight())

	def handleBtn_next_newDob(self, mainWindow, dataStruc):
		dataStruc.dob=self.inputedText
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "dob")==True):
			myUserSetup.myUserSetup.newUser_height(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handleBtn_next_newHeight(self, mainWindow, dataStruc):
		if (self.unit == "m"):
			dataStruc.height=self.inputedText
		else:
			dataStruc.height=str(float(self.inputedText)*0.3048)
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "height")==True):
			myUserSetup.myUserSetup.newUser_weight(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handleBtn_next_newWeight(self, mainWindow, dataStruc):
		if (self.unit == "k"):
			dataStruc.weight=self.inputedText
		else:
			dataStruc.weight=str(float(self.inputedText)*0.453)
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "weight")==True):
			myUserSetup.myUserSetup.newUser_passcode(self,mainWindow=mainWindow,newUserInfo=dataStruc)
	def handleBtn_next_editDob(self, mainWindow, dataStruc):
		dataStruc.dob=self.inputedText
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "dob")==True):
			myUserEdit.myUserEdit.editUser_height(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
	def handleBtn_next_editHeight(self, mainWindow, dataStruc):
		if (self.unit == "m"):
			dataStruc.height=self.inputedText
		else:
			dataStruc.height=str(float(self.inputedText)*0.3048)
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "height")==True):
			myUserEdit.myUserEdit.editUser_weight(self,mainWindow=mainWindow,currentUserInfo=dataStruc)
	def handleBtn_next_editWeight(self, mainWindow, dataStruc):
		if (self.unit == "k"):
			dataStruc.weight=self.inputedText
		else:
			dataStruc.weight=str(float(self.inputedText)*0.453)
		if(myCheckUserInfo.checkUserDetails(self,dataStruc, "weight")==True):
			myUserEdit.myUserEdit.editUser_add2db(self,mainWindow=mainWindow,currentUserInfo=dataStruc)

	def handle_btn_unit_height(self):
		if (self.unit == "m"):
			self.unit = "f"
			self.btn_unit.setText("Feet")
		else:
			self.unit = "m"
			self.btn_unit.setText("Meter")
	def handle_btn_unit_weight(self):
		if (self.unit == "k"):
			self.unit = "p"
			self.btn_unit.setText("lb")
		else:
			self.unit = "k"
			self.btn_unit.setText("kg")
	def updateLineEdit(self):
		self.lineEdit_currentText.setText(self.inputedText)
	def addNum2InputedText(self, num):
		self.inputedText += num
		self.updateLineEdit()
	def handleBtn_del(self):
		if(len(self.inputedText)>0):
			self.inputedText = self.inputedText[:(len(self.inputedText)-1)]
			if (("." not in self.inputedText)and(self.decimalEnable == True)):
				self.btn_dot.setEnabled(True)
			self.updateLineEdit()
	def handleBtn_0(self): self.addNum2InputedText('0')
	def handleBtn_1(self): self.addNum2InputedText('1')
	def handleBtn_2(self): self.addNum2InputedText('2')
	def handleBtn_3(self): self.addNum2InputedText('3')
	def handleBtn_4(self): self.addNum2InputedText('4')
	def handleBtn_5(self): self.addNum2InputedText('5')
	def handleBtn_6(self): self.addNum2InputedText('6')
	def handleBtn_7(self): self.addNum2InputedText('7')
	def handleBtn_8(self): self.addNum2InputedText('8')
	def handleBtn_9(self): self.addNum2InputedText('9')
	def handleBtn_dot(self):
		self.addNum2InputedText('.')
		self.btn_dot.setEnabled(False)

	def handleBtn_done_newPasscode(self):
		print(self.passcode)
