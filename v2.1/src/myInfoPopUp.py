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
        self.setStandardButtons(QMessageBox.Close)
        self.setWindowModality(Qt.NonModal)
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.closePopUp)
        self.timer.start()
        
    def closePopUp(self):
        self.timer.stop()
        self.close()
		
