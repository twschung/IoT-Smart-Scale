# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyse.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_analyse(object):
    def setupUi(self, analyse):
        analyse.setObjectName("analyse")
        analyse.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(analyse)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(analyse)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 3)
        self.btn_yes = QtWidgets.QPushButton(analyse)
        self.btn_yes.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_yes.setFont(font)
        self.btn_yes.setObjectName("btn_yes")
        self.gridLayout.addWidget(self.btn_yes, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(152, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_no = QtWidgets.QPushButton(analyse)
        self.btn_no.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_no.setFont(font)
        self.btn_no.setObjectName("btn_no")
        self.gridLayout.addWidget(self.btn_no, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(152, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.btn_tare = QtWidgets.QPushButton(analyse)
        self.btn_tare.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_tare.setFont(font)
        self.btn_tare.setObjectName("btn_tare")
        self.gridLayout.addWidget(self.btn_tare, 2, 4, 1, 1)
        self.lbl_title = QtWidgets.QLabel(analyse)
        self.lbl_title.setMinimumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 2, 1, 1)

        self.retranslateUi(analyse)
        QtCore.QMetaObject.connectSlotsByName(analyse)

    def retranslateUi(self, analyse):
        _translate = QtCore.QCoreApplication.translate
        analyse.setWindowTitle(_translate("analyse", "analyse"))
        self.btn_yes.setText(_translate("analyse", "Yes"))
        self.btn_no.setText(_translate("analyse", "No"))
        self.btn_tare.setText(_translate("analyse", "Tare"))
        self.lbl_title.setText(_translate("analyse", "Analyse this?"))

