import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import myMainMenu, myLoginMenu
import ui_mainmenu, ui_loginmenu, ui_foodinformation, ui_scaleonly, ui_usersetup, ui_passcode

class myMainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(myMainWindow, self).__init__(parent)
		self.setObjectName("mainWindow")
		self.resize(800, 480)
		self.central_widget = QStackedWidget()
		self.setCentralWidget(self.central_widget)
		self.widget = myMainMenu.myMainMenu(self)
		self.central_widget.addWidget(self.widget)
		self.central_widget.setCurrentWidget(self.widget)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = myMainWindow()
	window.showMaximised()
	sys.exit(app.exec_())
