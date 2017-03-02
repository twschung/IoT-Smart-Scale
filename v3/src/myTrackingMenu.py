"""
Change the progress bar to int (from float) and check if the program runs correctly
"""
import sys,datetime
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebKitWidgets import *
import ui_trackingmenu, barchart
import db_access

today = datetime.datetime.utcnow()# - datetime.timedelta(days=51)

class myTrackingMenu(QWidget, ui_trackingmenu.Ui_trackingMenu):
	def __init__(self, mainWindow, name=None, currentUserInfo=None):
		super(myTrackingMenu, self).__init__()
		self.setupUi(self)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.tabWidget.setCurrentIndex(0) # forces the first tab to be displayed
		id = currentUserInfo.id #6
		gender = currentUserInfo.gender

		# tab 1 content
		self.todayIntake = db_access.user_getDailyIntake(id, today.strftime('%Y-%m-%d'))
		self.yesterdayIntake = db_access.user_getDailyIntake(id, ((today - datetime.timedelta(days=1)).strftime('%Y-%m-%d')))
		# print('%s - %s'%(today.strftime('%Y-%m-%d'),self.todayIntake.energy))
		# print('%s - %s'%(i_minus1.strftime('%Y-%m-%d'),self.yesterdayIntake.energy))
		if(gender == 'm'):
			self.progressBar_today.setRange(0,2500)
			self.progressBar_yesterday.setRange(0,2500)
		if(gender == 'f'):
			self.progressBar_today.setRange(0,2000)
			self.progressBar_yesterday.setRange(0,2000)

		if(self.todayIntake[0] == False):
			self.progressBar_today.setValue(0)
			self.lbl_today.setText("Today's calorie intake: Add Food")
		else:
			self.progressBar_today.setValue(float(self.todayIntake[1].energy))
			self.lbl_today.setText("Today's calorie intake: %.0f kcal" %(float(self.todayIntake[1].energy)))

		if(self.yesterdayIntake[0] == False):
			self.progressBar_yesterday.setValue(0)
			self.lbl_yesterday.setText('No Entry Found')
		else:
			self.progressBar_yesterday.setValue(float(self.yesterdayIntake[1].energy))
			self.lbl_yesterday.setText("Yesterday's calorie intake: %s kcal" %(self.yesterdayIntake[1].energy))

		#tab 2 content
		barchart.plot_weekly_label(self,today, currentUserInfo.id)#, )
		plot_dir = os.getcwd() + '/temp-plot.html' 
		print(plot_dir)
		print(QUrl.fromLocalFile(plot_dir))
		self.weekly_label.load(QUrl.fromLocalFile(plot_dir))
		#self.weekly_label.load(QUrl('file:///home/pi/Desktop/IoT-Smart-Scale/v3/temp-plot.html'))
		#self.weekly_label.s(QUrl('file:///temp-plot.html'))

		# tab 3 content
		self.monthly_label.load(QUrl('http://m.google.com/'))
		print(QUrl('http://m.google.com/'))
		# self.monthly_label.show()

	def handleBtn_back(self, mainWindow):
		#mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
		os.remove('temp-plot.html') # deletes the plot when back is pressed
		sys.exit()

	def plot_tab3(self, today): #, currentUserInfo):
		pass
