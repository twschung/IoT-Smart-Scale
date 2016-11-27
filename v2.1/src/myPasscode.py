import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_passcode

class myPasscode(QWidget, ui_passcode.Ui_passCode):
	def __init__(self, mainWindow, name=None, layoutSetting=None):
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
		if (layoutSetting == "newPasscode"):
			self.btn_forgot.setEnabled(False)
			self.btn_back.setEnabled(False)
			self.label.setText("Please Enter a New Passcode")
			self.btn_done.clicked.connect(lambda:self.handleBtn_done_newPasscode())
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

	def handleBtn_done_newPasscode(self):
		print(self.passcode)
