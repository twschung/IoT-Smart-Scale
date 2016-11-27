# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountsetting.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_accountSetting(object):
    def setupUi(self, accountSetting):
        accountSetting.setObjectName("accountSetting")
        accountSetting.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(accountSetting)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(accountSetting)
        self.label.setMinimumSize(QtCore.QSize(261, 71))
        self.label.setMaximumSize(QtCore.QSize(261, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_send = QtWidgets.QPushButton(accountSetting)
        self.btn_send.setMinimumSize(QtCore.QSize(281, 91))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_send.setFont(font)
        self.btn_send.setObjectName("btn_send")
        self.gridLayout.addWidget(self.btn_send, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_guest = QtWidgets.QPushButton(accountSetting)
        self.btn_guest.setMinimumSize(QtCore.QSize(281, 91))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_guest.setFont(font)
        self.btn_guest.setObjectName("btn_guest")
        self.gridLayout.addWidget(self.btn_guest, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(215, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        self.btn_back = QtWidgets.QPushButton(accountSetting)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 4, 3, 1, 1)

        self.retranslateUi(accountSetting)
        QtCore.QMetaObject.connectSlotsByName(accountSetting)

    def retranslateUi(self, accountSetting):
        _translate = QtCore.QCoreApplication.translate
        accountSetting.setWindowTitle(_translate("accountSetting", "accountSetting"))
        self.label.setText(_translate("accountSetting", "Account Setting"))
        self.btn_send.setText(_translate("accountSetting", "Profile"))
        self.btn_guest.setText(_translate("accountSetting", "Goal"))
        self.btn_back.setText(_translate("accountSetting", "Back"))

