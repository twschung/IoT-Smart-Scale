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
        searchItem.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(searchItem)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_myTracking = QtWidgets.QLabel(searchItem)
        self.lbl_myTracking.setMinimumSize(QtCore.QSize(781, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_myTracking.setFont(font)
        self.lbl_myTracking.setObjectName("lbl_myTracking")
        self.gridLayout.addWidget(self.lbl_myTracking, 0, 0, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(searchItem)
        self.lineEdit.setMinimumSize(QtCore.QSize(781, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.btn_search = QtWidgets.QPushButton(searchItem)
        self.btn_search.setMinimumSize(QtCore.QSize(151, 51))
        self.btn_search.setObjectName("btn_search")
        self.gridLayout.addWidget(self.btn_search, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(467, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_search_2 = QtWidgets.QPushButton(searchItem)
        self.btn_search_2.setMinimumSize(QtCore.QSize(151, 51))
        self.btn_search_2.setObjectName("btn_search_2")
        self.gridLayout.addWidget(self.btn_search_2, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 320, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)

        self.retranslateUi(searchItem)
        QtCore.QMetaObject.connectSlotsByName(searchItem)

    def retranslateUi(self, searchItem):
        _translate = QtCore.QCoreApplication.translate
        searchItem.setWindowTitle(_translate("searchItem", "searchItem"))
        self.lbl_myTracking.setText(_translate("searchItem", "Search your food item:"))
        self.btn_search.setText(_translate("searchItem", "Search"))
        self.btn_search_2.setText(_translate("searchItem", "Back"))

