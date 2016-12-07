import sys
sys.path.insert(0,"/home/pi/Desktop/v2.1/src")
sys.path.insert(0,"/home/pi/Desktop/v2.1/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_profile
import myUserEdit

class myUserProfile(QWidget, ui_profile.Ui_profile):
	def __init__(self, mainWindow, name=None,layoutSetting=None, currentUserInfo=None):
		super(myUserProfile, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
		self.btn_edit.clicked.connect(lambda:myUserEdit.myUserEdit.editUser_verifyPasscode(self,mainWindow=mainWindow,currentUserInfo=currentUserInfo))
		self.lbl__nameVal.setText(currentUserInfo.firstname+" "+currentUserInfo.lastname)
		self.lbl_emailVal.setText(currentUserInfo.email)
		if(currentUserInfo.gender == "m"):
			self.lbl_genderVal.setText("Male")
		else:
			self.lbl_genderVal.setText("Female")
		self.lbl_birthYearVal.setText(currentUserInfo.dob)
		self.lbl_heightVal.setText(currentUserInfo.height+"/"+str(round(float(currentUserInfo.height)*3.28084,2)))
		self.lbl_weightVal.setText(currentUserInfo.weight+"/"+str(round(float(currentUserInfo.weight)*2.20462,2)))
		#bmi = str(round((int(currentUserInfo.weight)/(int(currentUserInfo.height)/100))/(int(currentUserInfo.height)/100),2))
		#self.lbl_bmiVal.setText(bmi)
		#self.lbl_idealWeightVal = 
		#self.lbl_exerciseVal = 
		
