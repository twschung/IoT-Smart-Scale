# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountsetting.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
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
        self.btn_profile = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_profile.sizePolicy().hasHeightForWidth())
        self.btn_profile.setSizePolicy(sizePolicy)
        self.btn_profile.setMinimumSize(QtCore.QSize(281, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_profile.setFont(font)
        self.btn_profile.setObjectName("btn_profile")
        self.gridLayout_2.addWidget(self.btn_profile, 0, 0, 1, 1)
        self.btn_goal = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_goal.sizePolicy().hasHeightForWidth())
        self.btn_goal.setSizePolicy(sizePolicy)
        self.btn_goal.setMinimumSize(QtCore.QSize(281, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_goal.setFont(font)
        self.btn_goal.setObjectName("btn_goal")
        self.gridLayout_2.addWidget(self.btn_goal, 0, 1, 1, 1)
        self.btn_back = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_2.addWidget(self.btn_back, 1, 1, 1, 1)
        self.btn_passcode = QtWidgets.QPushButton(accountSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_passcode.sizePolicy().hasHeightForWidth())
        self.btn_passcode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_passcode.setFont(font)
        self.btn_passcode.setObjectName("btn_passcode")
        self.gridLayout_2.addWidget(self.btn_passcode, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.retranslateUi(accountSetting)
        QtCore.QMetaObject.connectSlotsByName(accountSetting)

    def retranslateUi(self, accountSetting):
        _translate = QtCore.QCoreApplication.translate
        accountSetting.setWindowTitle(_translate("accountSetting", "accountSetting"))
        self.label.setText(_translate("accountSetting", "Account Settings"))
        self.btn_profile.setText(_translate("accountSetting", "Profile"))
        self.btn_goal.setText(_translate("accountSetting", "Goal"))
        self.btn_back.setText(_translate("accountSetting", "Back"))
        self.btn_passcode.setText(_translate("accountSetting", "Passcode\n"
"Fingerprint"))

