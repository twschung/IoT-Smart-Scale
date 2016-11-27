# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(result)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(result)
        self.lbl_title.setMinimumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(result)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 340))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)
        self.btn_back = QtWidgets.QPushButton(result)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(487, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_back_2 = QtWidgets.QPushButton(result)
        self.btn_back_2.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back_2.setFont(font)
        self.btn_back_2.setObjectName("btn_back_2")
        self.gridLayout.addWidget(self.btn_back_2, 2, 2, 1, 1)

        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "result"))
        self.lbl_title.setText(_translate("result", "Result"))
        self.btn_back.setText(_translate("result", "Back"))
        self.btn_back_2.setText(_translate("result", "Enter"))

