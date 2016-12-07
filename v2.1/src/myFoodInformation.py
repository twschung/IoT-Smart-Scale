import sys
sys.path.insert(0,"/home/pi/Desktop/v2.1/src")
sys.path.insert(0,"/home/pi/Desktop/v2.1/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_foodinformation
import db_structure
import time

class myFoodInformation(QWidget, ui_foodinformation.Ui_foodInformation):
	def __init__(self, mainWindow, currentUserInfo, name=None, layoutSetting=None):
		super(myFoodInformation, self).__init__()
		self.setupUi(self)
		foodInfo = db_structure.foodDataStructure()
		userDailyIntakeInfo = db_structure.userDailyIntakeStructure()
		self.btn_new.setText("Scan")
		if (layoutSetting == "guest"):
			self.btn_addIntake.setEnabled(False)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_new.clicked.connect(lambda:self.handleBtn_scan(mainWindow))
		self.btn_tare.clicked.connect(lambda:self.handleBtn_tare(mainWindow))
		self.btn_addIntake.clicked.connect(lambda:self.handleBtn_addIntake(mainWindow))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_scan(self, mainWindow):
		pass
		'''
		# add camera modules stuff here
		self.lbl_energyVal.setText(foodInfo.energy)
		self.lbl_proteinVal.setText(foodInfo.protein)
		self.lbl_sugarVal.setText(foodInfo.sugars)
		self.lbl_fibreVal.setText(foodInfo.fibre)
		self.lbl_fatVal.setText(foodInfo.fat)
		self.lbl.saltVal.setText(foodInfo.salt)
		'''
	def handleBtn_tare(self, mainWindow):
		pass
		# add tare stuff here
	def handleBtn_addIntake(self, mainWindow):
		pass
		'''
		userDailyIntakeInfo.userid = currentUserInfo.username
		userDailyIntakeInfo.date = time.strftime("%d/%m/%Y")
		userDailyIntakeInfo.energy = foodInfo.energy
		userDailyIntakeInfo.fat = foodInfo.fat
		userDailyIntakeInfo.sugars = foodInfo.sugars
		userDailyIntakeInfo.fiber = foodInfo.fibre
		userDailyIntakeInfo.protein = foodInfo.protein
		userDailyIntakeInfo.salt = foodInfo.salt
		'''


