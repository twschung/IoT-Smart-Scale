import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import myNumInput
import ui_goal

class myGoal(QWidget, ui_goal.Ui_goal):
	def __init__(self, mainWindow, name=None, currentUserInfo = None):
		super(myGoal, self).__init__()
		self.setupUi(self)
		if(currentUserInfo.targetIntake == "" or currentUserInfo.targetIntake == None):
			self.lbl_recommendedIntakeVal.setText("Not entered")
		else:
			self.lbl_recommendedIntakeVal.setText(currentUserInfo.targetIntake)
		if(currentUserInfo.targetWeight == "" or currentUserInfo.targetWeight == None):
			self.lbl_recommendedWeightVal.setText("Not entered")
		else:
			self.lbl_recommendedWeightVal.setText(currentUserInfo.targetWeight)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_edit.clicked.connect(lambda:self.handleBtn_edit(mainWindow,currentUserInfo))
	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_edit(self, mainWindow,currentUserInfo):
		self.widget = myNumInput.myNumInput(mainWindow, None, "editUserTarget_weight",currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
	def handleBtn_next(self,mainWindow,currentUserInfo):
		self.widget = myNumInput.myNumInput(mainWindow, None, "editUserTarget_intake",currentUserInfo)
		mainWindow.central_widget.addWidget(self.widget)
		mainWindow.central_widget.setCurrentWidget(self.widget)
