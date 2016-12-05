import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui import ui_profile
from src import myUserEdit

class myUserProfile(QWidget, ui_profile.Ui_profile):
	def __init__(self, mainWindow, name=None,layoutSetting=None, currentUserInfo=None):
		super(myUserProfile, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
		self.btn_edit.clicked.connect(lambda:myUserEdit.myUserEdit.passcodeVerify(self,mainWindow=mainWindow,currentUserInfo=currentUserInfo))
