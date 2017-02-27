# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foodsuggestionmenu.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_foodSuggestionMenu(object):
    def setupUi(self, foodSuggestionMenu):
        foodSuggestionMenu.setObjectName("foodSuggestionMenu")
        foodSuggestionMenu.resize(805, 488)
        self.gridLayout = QtWidgets.QGridLayout(foodSuggestionMenu)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(foodSuggestionMenu)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(foodSuggestionMenu)
        self.scrollArea.setMinimumSize(QtCore.QSize(781, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 425))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(779, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_sug3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_sug3.setObjectName("lbl_sug3")
        self.gridLayout_3.addWidget(self.lbl_sug3, 1, 3, 1, 1)
        self.lbl_sug1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_sug1.setObjectName("lbl_sug1")
        self.gridLayout_3.addWidget(self.lbl_sug1, 1, 2, 1, 1)
        self.lbl_sug2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_sug2.setObjectName("lbl_sug2")
        self.gridLayout_3.addWidget(self.lbl_sug2, 2, 2, 1, 1)
        self.lbl_sug4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_sug4.setObjectName("lbl_sug4")
        self.gridLayout_3.addWidget(self.lbl_sug4, 2, 3, 1, 1)
        self.lbl_sug5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_sug5.setMinimumSize(QtCore.QSize(0, 200))
        self.lbl_sug5.setObjectName("lbl_sug5")
        self.gridLayout_3.addWidget(self.lbl_sug5, 1, 4, 1, 1)
        self.btn_Back = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_Back.setMinimumSize(QtCore.QSize(0, 200))
        self.btn_Back.setObjectName("btn_Back")
        self.gridLayout_3.addWidget(self.btn_Back, 2, 4, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(foodSuggestionMenu)
        QtCore.QMetaObject.connectSlotsByName(foodSuggestionMenu)

    def retranslateUi(self, foodSuggestionMenu):
        _translate = QtCore.QCoreApplication.translate
        foodSuggestionMenu.setWindowTitle(_translate("foodSuggestionMenu", "foodSuggestionMenu"))
        self.lbl_title.setText(_translate("foodSuggestionMenu", "Our suggested food items:"))
        self.lbl_sug3.setText(_translate("foodSuggestionMenu", "-"))
        self.lbl_sug1.setText(_translate("foodSuggestionMenu", "-"))
        self.lbl_sug2.setText(_translate("foodSuggestionMenu", "-"))
        self.lbl_sug4.setText(_translate("foodSuggestionMenu", "-"))
        self.lbl_sug5.setText(_translate("foodSuggestionMenu", "-"))
        self.btn_Back.setText(_translate("foodSuggestionMenu", "Back"))

