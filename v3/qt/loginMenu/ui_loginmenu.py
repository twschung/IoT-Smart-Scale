# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginmenu.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginMenu(object):
    def setupUi(self, loginMenu):
        loginMenu.setObjectName("loginMenu")
        loginMenu.resize(805, 488)
        self.gridLayout = QtWidgets.QGridLayout(loginMenu)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(loginMenu)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(loginMenu)
        self.btn_back.setMinimumSize(QtCore.QSize(161, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        spacerItem = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_newLogin = QtWidgets.QPushButton(loginMenu)
        self.btn_newLogin.setMinimumSize(QtCore.QSize(161, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_newLogin.setFont(font)
        self.btn_newLogin.setObjectName("btn_newLogin")
        self.horizontalLayout.addWidget(self.btn_newLogin)
        self.btn_fingerprint = QtWidgets.QPushButton(loginMenu)
        self.btn_fingerprint.setMinimumSize(QtCore.QSize(161, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_fingerprint.setFont(font)
        self.btn_fingerprint.setObjectName("btn_fingerprint")
        self.horizontalLayout.addWidget(self.btn_fingerprint)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(loginMenu)
        self.scrollArea.setMinimumSize(QtCore.QSize(781, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 334))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(779, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_user5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_user5.setEnabled(False)
        self.btn_user5.setMinimumSize(QtCore.QSize(250, 161))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_user5.setFont(font)
        self.btn_user5.setObjectName("btn_user5")
        self.gridLayout_3.addWidget(self.btn_user5, 1, 1, 1, 1)
        self.btn_user6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_user6.setEnabled(False)
        self.btn_user6.setMinimumSize(QtCore.QSize(250, 161))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_user6.setFont(font)
        self.btn_user6.setObjectName("btn_user6")
        self.gridLayout_3.addWidget(self.btn_user6, 1, 2, 1, 1)
        self.btn_user1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_user1.setEnabled(False)
        self.btn_user1.setMinimumSize(QtCore.QSize(250, 161))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_user1.setFont(font)
        self.btn_user1.setObjectName("btn_user1")
        self.gridLayout_3.addWidget(self.btn_user1, 0, 0, 1, 1)
        self.btn_user2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_user2.setEnabled(False)
        self.btn_user2.setMinimumSize(QtCore.QSize(250, 161))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_user2.setFont(font)
        self.btn_user2.setObjectName("btn_user2")
        self.gridLayout_3.addWidget(self.btn_user2, 0, 1, 1, 1)
        self.btn_user3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_user3.setEnabled(False)
        self.btn_user3.setMinimumSize(QtCore.QSize(250, 161))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_user3.setFont(font)
        self.btn_user3.setObjectName("btn_user3")
        self.gridLayout_3.addWidget(self.btn_user3, 0, 2, 1, 1)
        self.btn_user4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_user4.setEnabled(False)
        self.btn_user4.setMinimumSize(QtCore.QSize(250, 161))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_user4.setFont(font)
        self.btn_user4.setObjectName("btn_user4")
        self.gridLayout_3.addWidget(self.btn_user4, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.scrollArea.raise_()
        self.lbl_title.raise_()

        self.retranslateUi(loginMenu)
        QtCore.QMetaObject.connectSlotsByName(loginMenu)

    def retranslateUi(self, loginMenu):
        _translate = QtCore.QCoreApplication.translate
        loginMenu.setWindowTitle(_translate("loginMenu", "Form"))
        self.lbl_title.setText(_translate("loginMenu", "Login"))
        self.btn_back.setText(_translate("loginMenu", "Back"))
        self.btn_newLogin.setText(_translate("loginMenu", "Username\n"
"Login"))
        self.btn_fingerprint.setText(_translate("loginMenu", "Fingerprint\n"
"Login"))
        self.btn_user5.setText(_translate("loginMenu", "-"))
        self.btn_user6.setText(_translate("loginMenu", "-"))
        self.btn_user1.setText(_translate("loginMenu", "-"))
        self.btn_user2.setText(_translate("loginMenu", "-"))
        self.btn_user3.setText(_translate("loginMenu", "-"))
        self.btn_user4.setText(_translate("loginMenu", "-"))

