import sys,datetime
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_trackingmenu, barchart

i = datetime.datetime.utcnow()

class myTrackingMenu(QWidget, ui_trackingmenu.Ui_trackingMenu):
	def __init__(self, mainWindow, currentUserInfo, name=None):
		super(myTrackingMenu, self).__init__()
		self.setupUi(self)

		self.tabWidget.setCurrentIndex(0) # forces the first tab to be displayed

		self.plot_weekly_graph(currentUserInfo)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))

	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		# sys.exit()

	def plot_weekly_graph(self, currentUserInfo):
		barchart.plot_weekly_label(self, currentUserInfo)
		self.weekly_graph = (QPixmap('weekly.png').scaledToHeight(self.weekly_frame.height()/1.1))
		# self.weekly_frame.frameGeometry().height()
		self.weekly_label.setPixmap(self.weekly_graph)
		# print(self.weekly_frame.height())
