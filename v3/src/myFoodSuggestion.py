import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_foodsuggestionmenu
import db_access, db_structure
currentDir = os.getcwd()

class myFoodSuggestion(QWidget, ui_foodsuggestionmenu.Ui_foodSuggestionMenu):
    def __init__(self, mainWindow, currentUserInfo, clfResult_prob, foodWeight):
        super(myFoodSuggestion, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.currentUserInfo = currentUserInfo
        self.foodWeight = foodWeight
        self.btn_Back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
        if (len(clfResult_prob)>0):
            s = str(clfResult_prob[0][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug1.width(), self.lbl_sug1.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug1.setPixmap(scaledPic)
            foodInfo = db_access.food_getInfo_localDB(clfResult_prob[0][0])[1]
            self.btn_sug1.setText(foodInfo.description)
            self.btn_sug1.clicked.connect(lambda: self.handleAddIntake(mainWindow,clfResult_prob[0][0]))
        if (len(clfResult_prob)>1):
            s = str(clfResult_prob[1][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug2.width(), self.lbl_sug2.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug2.setPixmap(scaledPic)
            foodInfo = db_access.food_getInfo_localDB(clfResult_prob[1][0])[1]
            self.btn_sug2.setText(foodInfo.description)
            self.btn_sug2.clicked.connect(lambda: self.handleAddIntake(mainWindow,clfResult_prob[1][0]))
        if (len(clfResult_prob)>2):
            s = str(clfResult_prob[2][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug3.width(), self.lbl_sug3.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug3.setPixmap(scaledPic)
            foodInfo = db_access.food_getInfo_localDB(clfResult_prob[2][0])[1]
            self.btn_sug3.setText(foodInfo.description)
            self.btn_sug3.clicked.connect(lambda: self.handleAddIntake(mainWindow,clfResult_prob[2][0]))
        if (len(clfResult_prob)>3):
            s = str(clfResult_prob[3][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug4.width(), self.lbl_sug4.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug4.setPixmap(scaledPic)
            foodInfo = db_access.food_getInfo_localDB(clfResult_prob[3][0])[1]
            self.btn_sug4.setText(foodInfo.description)
            self.btn_sug4.clicked.connect(lambda: self.handleAddIntake(mainWindow,clfResult_prob[3][0]))
        if (len(clfResult_prob)>4):
            s = str(clfResult_prob[4][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug5.width(), self.lbl_sug5.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug5.setPixmap(scaledPic)
            foodInfo = db_access.food_getInfo_localDB(clfResult_prob[4][0])[1]
            self.btn_sug5.setText(foodInfo.description)
            self.btn_sug5.clicked.connect(lambda: self.handleAddIntake(mainWindow,clfResult_prob[4][0]))

    def handleAddIntake(self,mainWindow,foodID):
        foodInfo = db_access.food_getActualInfo(self.currentUserInfo.id,str(foodID),str(self.foodWeight))
        db_access.user_addNewFoodIntake(foodInfo)
        forgroundFilePath, backgroundFilePath = ftp_access.generateExisitingItemFilePath(foodInfo.foodid)
		shutil.copyfile(os.path.join(os.getcwd(),"background.jpg"),backgroundFilePath)
		shutil.copyfile(os.path.join(os.getcwd(),"forground.jpg"),forgroundFilePath)
        msg = QMessageBox.information(self, 'Added',"Food item has been added to your intake",QMessageBox.Ok)
        mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
