# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(mainMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblStatus = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout_2.addWidget(self.lblStatus, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnUserDetails = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUserDetails.sizePolicy().hasHeightForWidth())
        self.btnUserDetails.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.btnUserDetails.setFont(font)
        self.btnUserDetails.setObjectName("btnUserDetails")
        self.gridLayout.addWidget(self.btnUserDetails, 0, 0, 1, 1)
        self.btnChangePassword = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChangePassword.sizePolicy().hasHeightForWidth())
        self.btnChangePassword.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.btnChangePassword.setFont(font)
        self.btnChangePassword.setObjectName("btnChangePassword")
        self.gridLayout.addWidget(self.btnChangePassword, 1, 0, 1, 1)
        self.btnGetWeight = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGetWeight.sizePolicy().hasHeightForWidth())
        self.btnGetWeight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.btnGetWeight.setFont(font)
        self.btnGetWeight.setObjectName("btnGetWeight")
        self.gridLayout.addWidget(self.btnGetWeight, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.btnLogout = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogout.sizePolicy().hasHeightForWidth())
        self.btnLogout.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.btnLogout.setFont(font)
        self.btnLogout.setObjectName("btnLogout")
        self.gridLayout.addWidget(self.btnLogout, 1, 2, 1, 1)
        self.btnChangeUserDetail = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChangeUserDetail.sizePolicy().hasHeightForWidth())
        self.btnChangeUserDetail.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.btnChangeUserDetail.setFont(font)
        self.btnChangeUserDetail.setObjectName("btnChangeUserDetail")
        self.gridLayout.addWidget(self.btnChangeUserDetail, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        mainMenu.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "smartScaleGUI"))
        self.lblStatus.setText(_translate("mainMenu", "<html><head/><body><p><span style=\" font-size:18pt;\">lblStatus</span></p></body></html>"))
        self.btnUserDetails.setText(_translate("mainMenu", "User Details"))
        self.btnChangePassword.setText(_translate("mainMenu", "Change Password"))
        self.btnGetWeight.setText(_translate("mainMenu", "Get Weight"))
        self.pushButton_5.setText(_translate("mainMenu", "/"))
        self.btnLogout.setText(_translate("mainMenu", "Logout"))
        self.btnChangeUserDetail.setText(_translate("mainMenu", "Change User Detail"))

