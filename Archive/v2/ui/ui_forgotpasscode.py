# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotpasscode.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_forgotPasscode(object):
    def setupUi(self, forgotPasscode):
        forgotPasscode.setObjectName("forgotPasscode")
        forgotPasscode.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(forgotPasscode)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(forgotPasscode)
        self.lbl_title.setMinimumSize(QtCore.QSize(261, 71))
        self.lbl_title.setMaximumSize(QtCore.QSize(261, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.btn_send = QtWidgets.QPushButton(forgotPasscode)
        self.btn_send.setMinimumSize(QtCore.QSize(281, 121))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_send.setFont(font)
        self.btn_send.setObjectName("btn_send")
        self.gridLayout.addWidget(self.btn_send, 1, 1, 1, 1)
        self.btn_guest = QtWidgets.QPushButton(forgotPasscode)
        self.btn_guest.setMinimumSize(QtCore.QSize(281, 121))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_guest.setFont(font)
        self.btn_guest.setObjectName("btn_guest")
        self.gridLayout.addWidget(self.btn_guest, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(215, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.btn_back = QtWidgets.QPushButton(forgotPasscode)
        self.btn_back.setMinimumSize(QtCore.QSize(281, 121))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 3, 1, 1, 1)

        self.retranslateUi(forgotPasscode)
        QtCore.QMetaObject.connectSlotsByName(forgotPasscode)

    def retranslateUi(self, forgotPasscode):
        _translate = QtCore.QCoreApplication.translate
        forgotPasscode.setWindowTitle(_translate("forgotPasscode", "forgotPasscode"))
        self.lbl_title.setText(_translate("forgotPasscode", "Choose your option."))
        self.btn_send.setText(_translate("forgotPasscode", "Send reset code to email"))
        self.btn_guest.setText(_translate("forgotPasscode", "Use scale as guest"))
        self.btn_back.setText(_translate("forgotPasscode", "Back to login"))

