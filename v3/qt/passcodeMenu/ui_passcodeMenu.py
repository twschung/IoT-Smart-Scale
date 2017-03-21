# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passcodeMenu.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_passcodeMenu(object):
    def setupUi(self, passcodeMenu):
        passcodeMenu.setObjectName("passcodeMenu")
        passcodeMenu.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(passcodeMenu)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_changePasscode = QtWidgets.QPushButton(passcodeMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_changePasscode.sizePolicy().hasHeightForWidth())
        self.btn_changePasscode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.btn_changePasscode.setFont(font)
        self.btn_changePasscode.setObjectName("btn_changePasscode")
        self.gridLayout_2.addWidget(self.btn_changePasscode, 0, 0, 1, 1)
        self.btn_fingerprint = QtWidgets.QPushButton(passcodeMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fingerprint.sizePolicy().hasHeightForWidth())
        self.btn_fingerprint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.btn_fingerprint.setFont(font)
        self.btn_fingerprint.setObjectName("btn_fingerprint")
        self.gridLayout_2.addWidget(self.btn_fingerprint, 0, 1, 1, 1)
        self.btn_back = QtWidgets.QPushButton(passcodeMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_2.addWidget(self.btn_back, 1, 1, 1, 1)
        self.btn_rmUsrFromMenu = QtWidgets.QPushButton(passcodeMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rmUsrFromMenu.sizePolicy().hasHeightForWidth())
        self.btn_rmUsrFromMenu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.btn_rmUsrFromMenu.setFont(font)
        self.btn_rmUsrFromMenu.setObjectName("btn_rmUsrFromMenu")
        self.gridLayout_2.addWidget(self.btn_rmUsrFromMenu, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(passcodeMenu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(passcodeMenu)
        QtCore.QMetaObject.connectSlotsByName(passcodeMenu)

    def retranslateUi(self, passcodeMenu):
        _translate = QtCore.QCoreApplication.translate
        passcodeMenu.setWindowTitle(_translate("passcodeMenu", "passcodeMenu"))
        self.btn_changePasscode.setText(_translate("passcodeMenu", "Change Passcode"))
        self.btn_fingerprint.setText(_translate("passcodeMenu", "Finger Print"))
        self.btn_back.setText(_translate("passcodeMenu", "Back"))
        self.btn_rmUsrFromMenu.setText(_translate("passcodeMenu", "Remove User \n"
"from Login Menu"))
        self.label.setText(_translate("passcodeMenu", "Passcode & Fingerprint Menu"))

