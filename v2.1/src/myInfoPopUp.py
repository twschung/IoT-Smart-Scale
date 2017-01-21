import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class myInfoPopUp(QMessageBox):
    def __init__(self,title="",message="",parent = None):
        super(myInfoPopUp, self).__init__(parent)
        self.setWindowTitle(title)
        self.setText(message)
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.NoButton)
        self.setWindowModality(Qt.NonModal)
