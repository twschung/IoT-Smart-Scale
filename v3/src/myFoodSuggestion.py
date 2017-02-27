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
        self.btn_back.clicked.connect(lambda:mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget()))
        s = str(clfResult_prob[0][0])+".jpg"
        pic = QPixmap(currentDir+'/imageSample/'+s)
        scaledPic = pic.scaled(self.lbl_sug1.width(), self.lbl_sug1.height(),Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
        self.lbl_sug1.setPixmap(scaledPic)
