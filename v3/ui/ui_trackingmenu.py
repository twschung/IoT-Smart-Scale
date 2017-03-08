# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trackingmenu.ui'
#
# Created: Wed Mar  8 13:22:46 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_trackingMenu(object):
    def setupUi(self, trackingMenu):
        trackingMenu.setObjectName("trackingMenu")
        trackingMenu.resize(800, 526)
        trackingMenu.setMaximumSize(QtCore.QSize(800, 526))
        self.gridLayout = QtWidgets.QGridLayout(trackingMenu)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_back = QtWidgets.QPushButton(trackingMenu)
        self.btn_back.setMinimumSize(QtCore.QSize(131, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(trackingMenu)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(100, 100))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_dailyRecord = QtWidgets.QWidget()
        self.tab_dailyRecord.setObjectName("tab_dailyRecord")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_dailyRecord)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 116, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar_today = QtWidgets.QProgressBar(self.tab_dailyRecord)
        self.progressBar_today.setProperty("value", 24)
        self.progressBar_today.setObjectName("progressBar_today")
        self.gridLayout_2.addWidget(self.progressBar_today, 1, 0, 1, 1)
        self.lbl_today = QtWidgets.QLabel(self.tab_dailyRecord)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_today.setFont(font)
        self.lbl_today.setObjectName("lbl_today")
        self.gridLayout_2.addWidget(self.lbl_today, 0, 0, 1, 1)
        self.lbl_yesterday = QtWidgets.QLabel(self.tab_dailyRecord)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_yesterday.setFont(font)
        self.lbl_yesterday.setObjectName("lbl_yesterday")
        self.gridLayout_2.addWidget(self.lbl_yesterday, 0, 1, 1, 1)
        self.progressBar_yesterday = QtWidgets.QProgressBar(self.tab_dailyRecord)
        self.progressBar_yesterday.setProperty("value", 24)
        self.progressBar_yesterday.setInvertedAppearance(False)
        self.progressBar_yesterday.setObjectName("progressBar_yesterday")
        self.gridLayout_2.addWidget(self.progressBar_yesterday, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 115, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_dailyRecord, "")
        self.tab_weeklyRecord = QtWidgets.QWidget()
        self.tab_weeklyRecord.setObjectName("tab_weeklyRecord")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_weeklyRecord)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_week = QtWidgets.QLabel(self.tab_weeklyRecord)
        self.lbl_week.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_week.setFont(font)
        self.lbl_week.setObjectName("lbl_week")
        self.gridLayout_4.addWidget(self.lbl_week, 0, 0, 1, 1)
        self.weekly_frame = QtWidgets.QFrame(self.tab_weeklyRecord)
        self.weekly_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weekly_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weekly_frame.setObjectName("weekly_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.weekly_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.weekly_label = QtWidgets.QLabel(self.weekly_frame)
        self.weekly_label.setObjectName("weekly_label")
        self.horizontalLayout_2.addWidget(self.weekly_label)
        self.gridLayout_4.addWidget(self.weekly_frame, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_weeklyRecord, "")
        self.tab_monthlyRecord = QtWidgets.QWidget()
        self.tab_monthlyRecord.setObjectName("tab_monthlyRecord")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_monthlyRecord)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_month = QtWidgets.QLabel(self.tab_monthlyRecord)
        self.lbl_month.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_month.setFont(font)
        self.lbl_month.setObjectName("lbl_month")
        self.verticalLayout.addWidget(self.lbl_month)
        self.monthly_frame = QtWidgets.QFrame(self.tab_monthlyRecord)
        self.monthly_frame.setMaximumSize(QtCore.QSize(705, 309))
        self.monthly_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monthly_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.monthly_frame.setObjectName("monthly_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.monthly_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.monthly_label = QtWebKitWidgets.QWebView(self.monthly_frame)
        self.monthly_label.setObjectName("monthly_label")
        self.horizontalLayout.addWidget(self.monthly_label)
        self.verticalLayout.addWidget(self.monthly_frame)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_monthlyRecord, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 2)
        self.lbl_title = QtWidgets.QLabel(trackingMenu)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(650, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)

        self.retranslateUi(trackingMenu)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(trackingMenu)

    def retranslateUi(self, trackingMenu):
        _translate = QtCore.QCoreApplication.translate
        trackingMenu.setWindowTitle(_translate("trackingMenu", "trackingMenu"))
        self.btn_back.setText(_translate("trackingMenu", "Back"))
        self.lbl_today.setText(_translate("trackingMenu", "Today\'s calorie intake"))
        self.lbl_yesterday.setText(_translate("trackingMenu", "Yesterday\'s calorie intake"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dailyRecord), _translate("trackingMenu", "Daily Record"))
        self.lbl_week.setText(_translate("trackingMenu", "This week\'s vs. last week\'s intake"))
        self.weekly_label.setText(_translate("trackingMenu", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_weeklyRecord), _translate("trackingMenu", "Weekly Record"))
        self.lbl_month.setText(_translate("trackingMenu", "This month\'s vs. last month\'s intake"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_monthlyRecord), _translate("trackingMenu", "Monthly Record"))
        self.lbl_title.setText(_translate("trackingMenu", "My Tracking"))

from PyQt5 import QtWebKitWidgets
