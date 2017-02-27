import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_foodsuggestionmenu
import db_access, db_structure
currentDir = os.getcwd()

class myFoodSuggestion(QWidget, ui_foodsuggestionmenu.Ui_foodSuggestionMenu):
    def __init__(self, mainWindow, currentUserInfo, clfResult_prob):
        super(myFoodSuggestion, self).__init__()
        self.setupUi(self)
        self.btn_Back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
        if (len(clfResult_prob)>0):
            s = str(clfResult_prob[0][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug1.width(), self.lbl_sug1.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug1.setPixmap(scaledPic)
        if (len(clfResult_prob)>1):
            s = str(clfResult_prob[1][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug2.width(), self.lbl_sug2.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug2.setPixmap(scaledPic)
        if (len(clfResult_prob)>2):
            s = str(clfResult_prob[2][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug3.width(), self.lbl_sug3.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug3.setPixmap(scaledPic)
        if (len(clfResult_prob)>3):
            s = str(clfResult_prob[3][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug4.width(), self.lbl_sug4.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug4.setPixmap(scaledPic)
        if (len(clfResult_prob)>4):
            s = str(clfResult_prob[4][0])+".jpg"
            pic = QPixmap(currentDir+'/imageSample/'+s)
            scaledPic = pic.scaled(self.lbl_sug5.width(), self.lbl_sug5.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
            self.lbl_sug5.setPixmap(scaledPic)
