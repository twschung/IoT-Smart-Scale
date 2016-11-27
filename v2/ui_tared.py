# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tared.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tared(object):
    def setupUi(self, tared):
        tared.setObjectName("tared")
        tared.resize(450, 300)
        self.gridLayout = QtWidgets.QGridLayout(tared)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(tared)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(tared)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(141, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.btn_back = QtWidgets.QPushButton(tared)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_3.addWidget(self.btn_back)
        spacerItem7 = QtWidgets.QSpacerItem(141, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.retranslateUi(tared)
        QtCore.QMetaObject.connectSlotsByName(tared)

    def retranslateUi(self, tared):
        _translate = QtCore.QCoreApplication.translate
        tared.setWindowTitle(_translate("tared", "tared"))
        self.label_2.setText(_translate("tared", "Tared."))
        self.label.setText(_translate("tared", "You may now place your food item."))
        self.btn_back.setText(_translate("tared", "Back"))

