# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passcodeMenu.ui'
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
        self.label.setMaximumSize(QtCore.QSize(400, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_changePasscode = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_changePasscode.sizePolicy().hasHeightForWidth())
        self.btn_changePasscode.setSizePolicy(sizePolicy)
        self.btn_changePasscode.setMinimumSize(QtCore.QSize(281, 91))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_changePasscode.setFont(font)
        self.btn_changePasscode.setObjectName("btn_changePasscode")
        self.gridLayout_2.addWidget(self.btn_changePasscode, 0, 0, 1, 1)
        self.btn_fingerprint = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fingerprint.sizePolicy().hasHeightForWidth())
        self.btn_fingerprint.setSizePolicy(sizePolicy)
        self.btn_fingerprint.setMinimumSize(QtCore.QSize(281, 91))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_fingerprint.setFont(font)
        self.btn_fingerprint.setObjectName("btn_fingerprint")
        self.gridLayout_2.addWidget(self.btn_fingerprint, 0, 1, 1, 1)
        self.btn_back = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_2.addWidget(self.btn_back, 1, 1, 1, 1)
        self.btn_rmUsrFromMenu = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rmUsrFromMenu.sizePolicy().hasHeightForWidth())
        self.btn_rmUsrFromMenu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_rmUsrFromMenu.setFont(font)
        self.btn_rmUsrFromMenu.setObjectName("btn_rmUsrFromMenu")
        self.gridLayout_2.addWidget(self.btn_rmUsrFromMenu, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.retranslateUi(accountSetting)
        QtCore.QMetaObject.connectSlotsByName(accountSetting)

    def retranslateUi(self, accountSetting):
        _translate = QtCore.QCoreApplication.translate
        accountSetting.setWindowTitle(_translate("accountSetting", "accountSetting"))
        self.label.setText(_translate("accountSetting", "Passcode & Finger Print Menu"))
        self.btn_changePasscode.setText(_translate("accountSetting", "Change Passcode"))
        self.btn_fingerprint.setText(_translate("accountSetting", "Finger Print"))
        self.btn_back.setText(_translate("accountSetting", "Back"))
        self.btn_rmUsrFromMenu.setText(_translate("accountSetting", "Remove User from Login Menu"))

