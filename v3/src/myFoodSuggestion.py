import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_foodsuggestionmenu
import db_access, db_structure

class myFoodSuggestion(QWidget, ui_foodsuggestionmenu.Ui_foodSuggestionMenu):
    def __init__(self, mainWindow, currentUserInfo, clfResult_prob):
        super(myFoodSuggestion, self).__init__()
        self.setupUi(self)
        print (clfResult_prob)
