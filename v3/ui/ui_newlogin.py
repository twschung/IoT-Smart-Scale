# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newlogin.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newLogin(object):
    def setupUi(self, newLogin):
        newLogin.setObjectName("newLogin")
        newLogin.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(newLogin)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(newLogin)
        self.lbl_title.setMinimumSize(QtCore.QSize(741, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(newLogin)
        self.groupBox.setMinimumSize(QtCore.QSize(741, 331))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lbl_email = QtWidgets.QLabel(self.groupBox)
        self.lbl_email.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_email.setFont(font)
        self.lbl_email.setObjectName("lbl_email")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_email)
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(513, 19))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_email)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.btn_back = QtWidgets.QPushButton(newLogin)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(487, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_login = QtWidgets.QPushButton(newLogin)
        self.btn_login.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.gridLayout.addWidget(self.btn_login, 2, 2, 1, 1)

        self.retranslateUi(newLogin)
        QtCore.QMetaObject.connectSlotsByName(newLogin)

    def retranslateUi(self, newLogin):
        _translate = QtCore.QCoreApplication.translate
        newLogin.setWindowTitle(_translate("newLogin", "newLogin"))
        self.lbl_title.setText(_translate("newLogin", "New Login"))
        self.lbl_email.setText(_translate("newLogin", "Email:"))
        self.btn_back.setText(_translate("newLogin", "Back"))
        self.btn_login.setText(_translate("newLogin", "Login"))

