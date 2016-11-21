# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scaleOnly.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_getWeight(object):
    def setupUi(self, getWeight):
        getWeight.setObjectName("getWeight")
        getWeight.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(getWeight)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(320, 90))
        self.frame.setMaximumSize(QtCore.QSize(320, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setContentsMargins(12, 11, 11, 11)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lcdWeight = QtWidgets.QLCDNumber(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lcdWeight.setFont(font)
        self.lcdWeight.setObjectName("lcdWeight")
        self.gridLayout_4.addWidget(self.lcdWeight, 0, 0, 1, 1)
        self.lblGrams = QtWidgets.QLabel(self.frame)
        self.lblGrams.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblGrams.setFont(font)
        self.lblGrams.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGrams.setObjectName("lblGrams")
        self.gridLayout_4.addWidget(self.lblGrams, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.btnBack = QtWidgets.QPushButton(self.centralWidget)
        self.btnBack.setMinimumSize(QtCore.QSize(160, 32))
        self.btnBack.setMaximumSize(QtCore.QSize(158, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 1, 0, 1, 1)
        getWeight.setCentralWidget(self.centralWidget)

        self.retranslateUi(getWeight)
        QtCore.QMetaObject.connectSlotsByName(getWeight)

    def retranslateUi(self, getWeight):
        _translate = QtCore.QCoreApplication.translate
        getWeight.setWindowTitle(_translate("getWeight", "smartScaleGUI"))
        self.lblGrams.setText(_translate("getWeight", "g"))
        self.btnBack.setText(_translate("getWeight", "Back"))

