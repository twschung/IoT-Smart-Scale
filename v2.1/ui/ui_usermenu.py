# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usermenu.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userMenu(object):
    def setupUi(self, userMenu):
        userMenu.setObjectName("userMenu")
        userMenu.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(userMenu)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_scanFood = QtWidgets.QPushButton(userMenu)
        self.btn_scanFood.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_scanFood.setFont(font)
        self.btn_scanFood.setObjectName("btn_scanFood")
        self.gridLayout.addWidget(self.btn_scanFood, 2, 1, 1, 1)
        self.btn_logout = QtWidgets.QPushButton(userMenu)
        self.btn_logout.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.gridLayout.addWidget(self.btn_logout, 3, 1, 1, 1)
        self.btn_myTracking = QtWidgets.QPushButton(userMenu)
        self.btn_myTracking.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_myTracking.setFont(font)
        self.btn_myTracking.setObjectName("btn_myTracking")
        self.gridLayout.addWidget(self.btn_myTracking, 2, 0, 1, 1)
        self.btn_accountSetting = QtWidgets.QPushButton(userMenu)
        self.btn_accountSetting.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_accountSetting.setFont(font)
        self.btn_accountSetting.setObjectName("btn_accountSetting")
        self.gridLayout.addWidget(self.btn_accountSetting, 3, 0, 1, 1)
        self.lbl_title = QtWidgets.QLabel(userMenu)
        self.lbl_title.setMinimumSize(QtCore.QSize(341, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)

        self.retranslateUi(userMenu)
        QtCore.QMetaObject.connectSlotsByName(userMenu)

    def retranslateUi(self, userMenu):
        _translate = QtCore.QCoreApplication.translate
        userMenu.setWindowTitle(_translate("userMenu", "userMenu"))
        self.btn_scanFood.setText(_translate("userMenu", "Scan Food"))
        self.btn_logout.setText(_translate("userMenu", "Logout"))
        self.btn_myTracking.setText(_translate("userMenu", "My Tracking"))
        self.btn_accountSetting.setText(_translate("userMenu", "Account Setting"))
        self.lbl_title.setText(_translate("userMenu", "Welcome Selena!"))

