# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchitem.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_searchItem(object):
    def setupUi(self, searchItem):
        searchItem.setObjectName("searchItem")
        searchItem.resize(805, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(searchItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_myTracking = QtWidgets.QLabel(searchItem)
        self.lbl_myTracking.setMinimumSize(QtCore.QSize(781, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_myTracking.setFont(font)
        self.lbl_myTracking.setObjectName("lbl_myTracking")
        self.verticalLayout.addWidget(self.lbl_myTracking)
        self.lineEdit = QtWidgets.QLineEdit(searchItem)
        self.lineEdit.setMinimumSize(QtCore.QSize(781, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(searchItem)
        self.btn_back.setMinimumSize(QtCore.QSize(151, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        spacerItem = QtWidgets.QSpacerItem(464, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_search = QtWidgets.QPushButton(searchItem)
        self.btn_search.setMinimumSize(QtCore.QSize(151, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 302, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(searchItem)
        QtCore.QMetaObject.connectSlotsByName(searchItem)

    def retranslateUi(self, searchItem):
        _translate = QtCore.QCoreApplication.translate
        searchItem.setWindowTitle(_translate("searchItem", "Form"))
        self.lbl_myTracking.setText(_translate("searchItem", "Search food item:"))
        self.btn_back.setText(_translate("searchItem", "Back"))
        self.btn_search.setText(_translate("searchItem", "Search"))

