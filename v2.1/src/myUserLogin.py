import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_newlogin
import myPasscode, myTextInput, myUserMenu
import db_structure, db_access
import numpy as np

class myUserLogin():
    def __init__(self, mainWindow, newUser=False):
        currentUserInfo = db_structure.userDataStructure()
        self.widget = myTextInput.myTextInput(mainWindow, layoutSetting = "loginUser_email", dataStruc=currentUserInfo)
        mainWindow.central_widget.addWidget(self.widget)
        mainWindow.central_widget.setCurrentWidget(self.widget)
    def loginUser_email(self, mainWindow, currentUserInfo):
        mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
        self.widget = myTextInput.myTextInput(mainWindow, layoutSetting = "loginUser_email", dataStruc=currentUserInfo)
        mainWindow.central_widget.addWidget(self.widget)
        mainWindow.central_widget.setCurrentWidget(self.widget)
    def loginUser_passcode(self, mainWindow, currentUserInfo, newUser):
        mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
        self.widget = myPasscode.myPasscode(mainWindow, layoutSetting = "loginUser_passcode", dataStruc=currentUserInfo, newUser=newUser)
        mainWindow.central_widget.addWidget(self.widget)
        mainWindow.central_widget.setCurrentWidget(self.widget)
    def enterUserMenu(self, mainWindow, currentUserInfo):
        mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
        self.widget = myUserMenu.myUserMenu(mainWindow, currentUserInfo=currentUserInfo)
        mainWindow.central_widget.addWidget(self.widget)
        mainWindow.central_widget.setCurrentWidget(self.widget)

    def checkRemeberUserStatus(self,currentUserInfo):
        self.config = np.load('config.npy').item()
        finishFlag = False
        for x in range(0,6):
            if (self.config['expUsr'][x].email == currentUserInfo.email): finishFlag = True
        return finishFlag

    def rememberUser(self,currentUserInfo):
        self.config = np.load('config.npy').item()
        finishFlag = False
        for x in range(0,6):
            if (self.config['expUsr'][x].id == currentUserInfo.id): finishFlag = True
        for x in range(0,6):
            if (finishFlag == False and self.config['expUsr'][x].id ==""):
                self.config['expUsr'][x] = currentUserInfo
                self.config['expUsr'][x].password = ""
                np.save('config.npy', self.config)
                finishFlag = True
        if (finishFlag == False): msg = QMessageBox.information(self, 'Failed',"Unable to assign user to login menu",QMessageBox.Ok)

    def forgetUser(self,currentUserInfo):
        self.config = np.load('config.npy').item()
        finishFlag = True
        for x in range(0,6):
            if (self.config['expUsr'][x].id == currentUserInfo.id): finishFlag = False
        for x in range(0,6):
            if (finishFlag == False and self.config['expUsr'][x].id == currentUserInfo.id):
                self.config['expUsr'][x] = db_structure.userDataStructure()
                np.save('config.npy', self.config)
                finishFlag = True
        if (finishFlag == False):
            msg = QMessageBox.information(self, 'Failed',"Unable to remove user from login menu",QMessageBox.Ok)
        else:
            msg = QMessageBox.information(self, 'Success',"Removed user from login menu",QMessageBox.Ok)

    def rememberUserAndFingerPrint(self,currentUserInfo):
        self.config = np.load('config.npy').item()
        finishFlag = False
        for x in range(0,6):
            if (self.config['expUsr'][x].id == currentUserInfo.id): finishFlag = True
        for x in range(0,6):
            if (finishFlag == False and self.config['expUsr'][x].id ==""):
                self.config['expUsr'][x] = currentUserInfo
                self.config['expUsr'][x].password = ""
                np.save('config.npy', self.config)
                finishFlag = True
        if (finishFlag == False):
            msg = QMessageBox.information(self, 'Failed',"Unable to assign user to login menu",QMessageBox.Ok)
        else:
            print("PWS")
