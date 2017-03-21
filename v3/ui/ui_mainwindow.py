# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(self.centralWidget)
        self.lbl_title.setMinimumSize(QtCore.QSize(341, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.btn_login = QtWidgets.QPushButton(self.centralWidget)
        self.btn_login.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.gridLayout.addWidget(self.btn_login, 1, 0, 1, 1)
        self.btn_guest = QtWidgets.QPushButton(self.centralWidget)
        self.btn_guest.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_guest.setFont(font)
        self.btn_guest.setObjectName("btn_guest")
        self.gridLayout.addWidget(self.btn_guest, 1, 1, 1, 1)
        self.btn_scaleOnly = QtWidgets.QPushButton(self.centralWidget)
        self.btn_scaleOnly.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_scaleOnly.setFont(font)
        self.btn_scaleOnly.setObjectName("btn_scaleOnly")
        self.gridLayout.addWidget(self.btn_scaleOnly, 2, 0, 1, 1)
        self.btn_userSetup = QtWidgets.QPushButton(self.centralWidget)
        self.btn_userSetup.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_userSetup.setFont(font)
        self.btn_userSetup.setObjectName("btn_userSetup")
        self.gridLayout.addWidget(self.btn_userSetup, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "IoT Smart Scale"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.btn_guest.setText(_translate("MainWindow", "Guest"))
        self.btn_scaleOnly.setText(_translate("MainWindow", "Scale Only"))
        self.btn_userSetup.setText(_translate("MainWindow", "User Setup"))

