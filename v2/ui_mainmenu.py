# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(mainMenu)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(mainMenu)
        self.lbl_title.setMinimumSize(QtCore.QSize(341, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.btn_login = QtWidgets.QPushButton(mainMenu)
        self.btn_login.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.gridLayout.addWidget(self.btn_login, 1, 0, 1, 1)
        self.btn_guest = QtWidgets.QPushButton(mainMenu)
        self.btn_guest.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_guest.setFont(font)
        self.btn_guest.setObjectName("btn_guest")
        self.gridLayout.addWidget(self.btn_guest, 1, 1, 1, 1)
        self.btn_scaleOnly = QtWidgets.QPushButton(mainMenu)
        self.btn_scaleOnly.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_scaleOnly.setFont(font)
        self.btn_scaleOnly.setObjectName("btn_scaleOnly")
        self.gridLayout.addWidget(self.btn_scaleOnly, 2, 0, 1, 1)
        self.btn_userSetup = QtWidgets.QPushButton(mainMenu)
        self.btn_userSetup.setMinimumSize(QtCore.QSize(341, 191))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_userSetup.setFont(font)
        self.btn_userSetup.setObjectName("btn_userSetup")
        self.gridLayout.addWidget(self.btn_userSetup, 2, 1, 1, 1)

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "mainMenu"))
        self.lbl_title.setText(_translate("mainMenu", "IoT Smart Scale"))
        self.btn_login.setText(_translate("mainMenu", "Login"))
        self.btn_guest.setText(_translate("mainMenu", "Guest"))
        self.btn_scaleOnly.setText(_translate("mainMenu", "Scale Only"))
        self.btn_userSetup.setText(_translate("mainMenu", "User Setup"))

