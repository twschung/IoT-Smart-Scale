# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_profile(object):
    def setupUi(self, profile):
        profile.setObjectName("profile")
        profile.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(profile)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(profile)
        self.lbl_title.setMinimumSize(QtCore.QSize(780, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(profile)
        self.groupBox.setMinimumSize(QtCore.QSize(741, 331))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lbl_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_name.setMinimumSize(QtCore.QSize(251, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.lbl__nameVal = QtWidgets.QLabel(self.groupBox)
        self.lbl__nameVal.setMinimumSize(QtCore.QSize(451, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl__nameVal.setFont(font)
        self.lbl__nameVal.setObjectName("lbl__nameVal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl__nameVal)
        self.lbl_email = QtWidgets.QLabel(self.groupBox)
        self.lbl_email.setMinimumSize(QtCore.QSize(251, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_email.setFont(font)
        self.lbl_email.setObjectName("lbl_email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_email)
        self.lbl_emailVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_emailVal.setMinimumSize(QtCore.QSize(451, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_emailVal.setFont(font)
        self.lbl_emailVal.setObjectName("lbl_emailVal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_emailVal)
        self.lbl_gender = QtWidgets.QLabel(self.groupBox)
        self.lbl_gender.setMinimumSize(QtCore.QSize(251, 19))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gender.setFont(font)
        self.lbl_gender.setObjectName("lbl_gender")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_gender)
        self.lbl_genderVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_genderVal.setMinimumSize(QtCore.QSize(451, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_genderVal.setFont(font)
        self.lbl_genderVal.setObjectName("lbl_genderVal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbl_genderVal)
        self.lbl_birthYear = QtWidgets.QLabel(self.groupBox)
        self.lbl_birthYear.setMinimumSize(QtCore.QSize(251, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_birthYear.setFont(font)
        self.lbl_birthYear.setObjectName("lbl_birthYear")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_birthYear)
        self.lbl_birthYearVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_birthYearVal.setMinimumSize(QtCore.QSize(451, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_birthYearVal.setFont(font)
        self.lbl_birthYearVal.setObjectName("lbl_birthYearVal")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lbl_birthYearVal)
        self.lbl_height = QtWidgets.QLabel(self.groupBox)
        self.lbl_height.setMinimumSize(QtCore.QSize(251, 19))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_height.setFont(font)
        self.lbl_height.setObjectName("lbl_height")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_height)
        self.lbl_heightVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_heightVal.setMinimumSize(QtCore.QSize(451, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_heightVal.setFont(font)
        self.lbl_heightVal.setObjectName("lbl_heightVal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lbl_heightVal)
        self.lbl_heightUnits = QtWidgets.QLabel(self.groupBox)
        self.lbl_heightUnits.setMinimumSize(QtCore.QSize(451, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_heightUnits.setFont(font)
        self.lbl_heightUnits.setObjectName("lbl_heightUnits")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lbl_heightUnits)
        self.lbl_weight = QtWidgets.QLabel(self.groupBox)
        self.lbl_weight.setMinimumSize(QtCore.QSize(251, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_weight.setFont(font)
        self.lbl_weight.setObjectName("lbl_weight")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_weight)
        self.lbl_weightVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_weightVal.setMinimumSize(QtCore.QSize(451, 19))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_weightVal.setFont(font)
        self.lbl_weightVal.setObjectName("lbl_weightVal")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lbl_weightVal)
        self.lbl_weightUnits = QtWidgets.QLabel(self.groupBox)
        self.lbl_weightUnits.setMinimumSize(QtCore.QSize(451, 19))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_weightUnits.setFont(font)
        self.lbl_weightUnits.setObjectName("lbl_weightUnits")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lbl_weightUnits)
        self.lbl_bmi = QtWidgets.QLabel(self.groupBox)
        self.lbl_bmi.setMinimumSize(QtCore.QSize(251, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_bmi.setFont(font)
        self.lbl_bmi.setObjectName("lbl_bmi")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lbl_bmi)
        self.lbl_bmiVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_bmiVal.setMinimumSize(QtCore.QSize(451, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_bmiVal.setFont(font)
        self.lbl_bmiVal.setObjectName("lbl_bmiVal")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lbl_bmiVal)
        self.lbl_idealWeight = QtWidgets.QLabel(self.groupBox)
        self.lbl_idealWeight.setMinimumSize(QtCore.QSize(251, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_idealWeight.setFont(font)
        self.lbl_idealWeight.setObjectName("lbl_idealWeight")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lbl_idealWeight)
        self.lbl_idealWeightVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_idealWeightVal.setMinimumSize(QtCore.QSize(451, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_idealWeightVal.setFont(font)
        self.lbl_idealWeightVal.setObjectName("lbl_idealWeightVal")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lbl_idealWeightVal)
        self.lbl_exercise = QtWidgets.QLabel(self.groupBox)
        self.lbl_exercise.setMinimumSize(QtCore.QSize(251, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_exercise.setFont(font)
        self.lbl_exercise.setObjectName("lbl_exercise")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lbl_exercise)
        self.lbl_exerciseVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_exerciseVal.setMinimumSize(QtCore.QSize(451, 20))
        self.lbl_exerciseVal.setMaximumSize(QtCore.QSize(481, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_exerciseVal.setFont(font)
        self.lbl_exerciseVal.setObjectName("lbl_exerciseVal")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lbl_exerciseVal)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.btn_back = QtWidgets.QPushButton(profile)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(487, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_edit = QtWidgets.QPushButton(profile)
        self.btn_edit.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")
        self.gridLayout.addWidget(self.btn_edit, 2, 2, 1, 1)

        self.retranslateUi(profile)
        QtCore.QMetaObject.connectSlotsByName(profile)

    def retranslateUi(self, profile):
        _translate = QtCore.QCoreApplication.translate
        profile.setWindowTitle(_translate("profile", "profile"))
        self.lbl_title.setText(_translate("profile", "Profile"))
        self.lbl_name.setText(_translate("profile", "Name:"))
        self.lbl__nameVal.setText(_translate("profile", "Name"))
        self.lbl_email.setText(_translate("profile", "Email:"))
        self.lbl_emailVal.setText(_translate("profile", "Email"))
        self.lbl_gender.setText(_translate("profile", "Gender:"))
        self.lbl_genderVal.setText(_translate("profile", "Gender"))
        self.lbl_birthYear.setText(_translate("profile", "Birth Year:"))
        self.lbl_birthYearVal.setText(_translate("profile", "Birth Year"))
        self.lbl_height.setText(_translate("profile", "Height:"))
        self.lbl_heightVal.setText(_translate("profile", "Height"))
        self.lbl_heightUnits.setText(_translate("profile", "cm/ ft"))
        self.lbl_weight.setText(_translate("profile", "Weight:"))
        self.lbl_weightVal.setText(_translate("profile", "Weight"))
        self.lbl_weightUnits.setText(_translate("profile", "kg/ lb"))
        self.lbl_bmi.setText(_translate("profile", "BMI:"))
        self.lbl_bmiVal.setText(_translate("profile", "BMI"))
        self.lbl_idealWeight.setText(_translate("profile", "Ideal Weight: "))
        self.lbl_idealWeightVal.setText(_translate("profile", "Ideal Weight"))
        self.lbl_exercise.setText(_translate("profile", "Recommended Exercise:"))
        self.lbl_exerciseVal.setText(_translate("profile", "kcal"))
        self.btn_back.setText(_translate("profile", "Back"))
        self.btn_edit.setText(_translate("profile", "Edit"))
