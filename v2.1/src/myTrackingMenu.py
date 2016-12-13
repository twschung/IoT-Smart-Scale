import sys,datetime
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_trackingmenu, barchart

i = datetime.datetime.utcnow()
i_minus1 = i - datetime.timedelta(days=1)

class myTrackingMenu(QWidget, ui_trackingmenu.Ui_trackingMenu):
	def __init__(self, mainWindow, currentUserInfo, name=None):
		super(myTrackingMenu, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.tabWidget.setCurrentIndex(0) # forces the first tab to be displayed

		# tab 1 content
		self.todayIntake = db_access.user_getDailyIntake(currentUserInfoid, i.strftime('%Y-%m-%d'))[1]
		self.yesterdayIntake = db_access.user_getDailyIntake(currentUserInfo.id, (i_minus1.strftime('%Y-%m-%d')))[1]
		# print('%s - %s'%(i.strftime('%Y-%m-%d'),self.todayIntake.energy))
		# print('%s - %s'%(i_minus1.strftime('%Y-%m-%d'),self.yesterdayIntake.energy))
		if(currentUserInfo.gender == 'm'):
			self.progressBar_today.setRange(0,2500)
			self.progressBar_yesterday.setRange(0,2500)
		if(currentUserInfo.gender == 'f'):
			self.progressBar_today.setRange(0,2000)
			self.progressBar_yesterday.setRange(0,2000)
		self.progressBar_today.setValue(int(self.todayIntake.energy))
		self.lbl_today.setText("Today's calorie intake: %s kcal" %(self.todayIntake.energy))
		self.progressBar_yesterday.setValue(int(self.yesterdayIntake.energy))
		self.lbl_yesterday.setText("Yesterday's calorie intake: %s kcal" %(self.yesterdayIntake.energy))

		#tab 2 content
		self.plot_weekly_graph(currentUserInfo)

		# tab 3 content


	def handleBtn_back(self, mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		# sys.exit()

	def plot_weekly_graph(self, currentUserInfo):
		barchart.plot_weekly_label(self, currentUserInfo)
		self.weekly_graph = (QPixmap('weekly.png').scaledToHeight(self.weekly_frame.height()/1.1))
		# self.weekly_frame.frameGeometry().height()
		self.weekly_label.setPixmap(self.weekly_graph)
		# print(self.weekly_frame.height())
