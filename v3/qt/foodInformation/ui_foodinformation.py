# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foodinformation.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_foodInformation(object):
    def setupUi(self, foodInformation):
        foodInformation.setObjectName("foodInformation")
        foodInformation.resize(800, 490)
        font = QtGui.QFont()
        font.setPointSize(24)
        foodInformation.setFont(font)
        self.gridLayout_3 = QtWidgets.QGridLayout(foodInformation)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_lcd = QtWidgets.QFrame(foodInformation)
        self.frame_lcd.setMinimumSize(QtCore.QSize(321, 101))
        self.frame_lcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lcd.setObjectName("frame_lcd")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_lcd)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcd_number = QtWidgets.QLCDNumber(self.frame_lcd)
        self.lcd_number.setMinimumSize(QtCore.QSize(311, 81))
        self.lcd_number.setObjectName("lcd_number")
        self.gridLayout_2.addWidget(self.lcd_number, 0, 0, 1, 1)
        self.lbl_g = QtWidgets.QLabel(self.frame_lcd)
        self.lbl_g.setMinimumSize(QtCore.QSize(21, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_g.setFont(font)
        self.lbl_g.setObjectName("lbl_g")
        self.gridLayout_2.addWidget(self.lbl_g, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_lcd, 4, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 6, 0, 1, 1)
        self.btn_back = QtWidgets.QPushButton(foodInformation)
        self.btn_back.setMinimumSize(QtCore.QSize(161, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_back.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_3.addWidget(self.btn_back, 5, 2, 1, 1)
        self.lbl_title = QtWidgets.QLabel(foodInformation)
        self.lbl_title.setMinimumSize(QtCore.QSize(231, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout_3.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.grpBx_nutriInfo = QtWidgets.QGroupBox(foodInformation)
        self.grpBx_nutriInfo.setMinimumSize(QtCore.QSize(201, 298))
        self.grpBx_nutriInfo.setTitle("")
        self.grpBx_nutriInfo.setObjectName("grpBx_nutriInfo")
        self.gridLayout = QtWidgets.QGridLayout(self.grpBx_nutriInfo)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_energy = QtWidgets.QLabel(self.grpBx_nutriInfo)
        self.lbl_energy.setMinimumSize(QtCore.QSize(91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_energy.setFont(font)
        self.lbl_energy.setObjectName("lbl_energy")
        self.gridLayout.addWidget(self.lbl_energy, 0, 0, 1, 1)
        self.lbl_evergyVal = QtWidgets.QLabel(self.grpBx_nutriInfo)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_evergyVal.setFont(font)
        self.lbl_evergyVal.setText("")
        self.lbl_evergyVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_evergyVal.setObjectName("lbl_evergyVal")
        self.gridLayout.addWidget(self.lbl_evergyVal, 0, 1, 1, 1)
        self.lbl_protein = QtWidgets.QLabel(self.grpBx_nutriInfo)
        self.lbl_protein.setMinimumSize(QtCore.QSize(91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_protein.setFont(font)
        self.lbl_protein.setObjectName("lbl_protein")
        self.gridLayout.addWidget(self.lbl_protein, 1, 0, 1, 1)
        self.lbl_proteinVal = QtWidgets.QLabel(self.grpBx_nutriInfo)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_proteinVal.setFont(font)
        self.lbl_proteinVal.setText("")
        self.lbl_proteinVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_proteinVal.setObjectName("lbl_proteinVal")
        self.gridLayout.addWidget(self.lbl_proteinVal, 1, 1, 1, 1)
        self.lbl_sugar = QtWidgets.QLabel(self.grpBx_nutriInfo)
        self.lbl_sugar.setMinimumSize(QtCore.QSize(91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_sugar.setFont(font)
        self.lbl_sugar.setObjectName("lbl_sugar")
        self.gridLayout.addWidget(self.lbl_sugar, 2, 0, 1, 1)
        self.lbl_sugarVal = QtWidgets.QLabel(self.grpBx_nutriInfo)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_sugarVal.setFont(font)
        self.lbl_sugarVal.setText("")
        self.lbl_sugarVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_sugarVal.setObjectName("lbl_sugarVal")
        self.gridLayout.addWidget(self.lbl_sugarVal, 2, 1, 1, 1)
        self.lbl_fibre = QtWidgets.QLabel(self.grpBx_nutriInfo)
        self.lbl_fibre.setMinimumSize(QtCore.QSize(91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_fibre.setFont(font)
        self.lbl_fibre.setObjectName("lbl_fibre")
        self.gridLayout.addWidget(self.lbl_fibre, 3, 0, 1, 1)
        self.lbl_fibreVal = QtWidgets.QLabel(self.grpBx_nutriInfo)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_fibreVal.setFont(font)
        self.lbl_fibreVal.setText("")
        self.lbl_fibreVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_fibreVal.setObjectName("lbl_fibreVal")
        self.gridLayout.addWidget(self.lbl_fibreVal, 3, 1, 1, 1)
        self.lbl_fat = QtWidgets.QLabel(self.grpBx_nutriInfo)
        self.lbl_fat.setMinimumSize(QtCore.QSize(91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_fat.setFont(font)
        self.lbl_fat.setObjectName("lbl_fat")
        self.gridLayout.addWidget(self.lbl_fat, 4, 0, 1, 1)
        self.lbl_fatVal = QtWidgets.QLabel(self.grpBx_nutriInfo)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_fatVal.setFont(font)
        self.lbl_fatVal.setText("")
        self.lbl_fatVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_fatVal.setObjectName("lbl_fatVal")
        self.gridLayout.addWidget(self.lbl_fatVal, 4, 1, 1, 1)
        self.lbl_salt = QtWidgets.QLabel(self.grpBx_nutriInfo)
        self.lbl_salt.setMinimumSize(QtCore.QSize(91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_salt.setFont(font)
        self.lbl_salt.setObjectName("lbl_salt")
        self.gridLayout.addWidget(self.lbl_salt, 5, 0, 1, 1)
        self.lbl_saltVal = QtWidgets.QLabel(self.grpBx_nutriInfo)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.lbl_saltVal.setFont(font)
        self.lbl_saltVal.setText("")
        self.lbl_saltVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_saltVal.setObjectName("lbl_saltVal")
        self.gridLayout.addWidget(self.lbl_saltVal, 5, 1, 1, 1)
        self.gridLayout_3.addWidget(self.grpBx_nutriInfo, 1, 2, 1, 1)
        self.btn_new = QtWidgets.QPushButton(foodInformation)
        self.btn_new.setMinimumSize(QtCore.QSize(101, 110))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_new.setFont(font)
        self.btn_new.setObjectName("btn_new")
        self.gridLayout_3.addWidget(self.btn_new, 4, 1, 2, 1)
        self.lbl_foodPic = QtWidgets.QLabel(foodInformation)
        self.lbl_foodPic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_foodPic.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_foodPic.setObjectName("lbl_foodPic")
        self.gridLayout_3.addWidget(self.lbl_foodPic, 1, 0, 1, 2)
        self.btn_tare = QtWidgets.QPushButton(foodInformation)
        self.btn_tare.setMinimumSize(QtCore.QSize(101, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_tare.setFont(font)
        self.btn_tare.setObjectName("btn_tare")
        self.gridLayout_3.addWidget(self.btn_tare, 4, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_suggestion = QtWidgets.QPushButton(foodInformation)
        self.btn_suggestion.setMinimumSize(QtCore.QSize(161, 51))
        self.btn_suggestion.setObjectName("btn_suggestion")
        self.horizontalLayout.addWidget(self.btn_suggestion)
        self.btn_addIntake = QtWidgets.QPushButton(foodInformation)
        self.btn_addIntake.setMinimumSize(QtCore.QSize(161, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_addIntake.setFont(font)
        self.btn_addIntake.setObjectName("btn_addIntake")
        self.horizontalLayout.addWidget(self.btn_addIntake)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 2)

        self.retranslateUi(foodInformation)
        QtCore.QMetaObject.connectSlotsByName(foodInformation)

    def retranslateUi(self, foodInformation):
        _translate = QtCore.QCoreApplication.translate
        foodInformation.setWindowTitle(_translate("foodInformation", "foodInformation"))
        self.lbl_g.setText(_translate("foodInformation", "g"))
        self.btn_back.setText(_translate("foodInformation", "Back"))
        self.lbl_title.setText(_translate("foodInformation", "Food Item Information"))
        self.lbl_energy.setText(_translate("foodInformation", "Energy (kcal)"))
        self.lbl_protein.setText(_translate("foodInformation", "Protein (g)"))
        self.lbl_sugar.setText(_translate("foodInformation", "Sugar (g)"))
        self.lbl_fibre.setText(_translate("foodInformation", "Fibre (g)"))
        self.lbl_fat.setText(_translate("foodInformation", "Fat (g)"))
        self.lbl_salt.setText(_translate("foodInformation", "Salt (g)"))
        self.btn_new.setText(_translate("foodInformation", "New"))
        self.lbl_foodPic.setText(_translate("foodInformation", "Picture"))
        self.btn_tare.setText(_translate("foodInformation", "Tare"))
        self.btn_suggestion.setText(_translate("foodInformation", "Incorrect"))
        self.btn_addIntake.setText(_translate("foodInformation", "Correct"))

