# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goal.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_goal(object):
    def setupUi(self, goal):
        goal.setObjectName("goal")
        goal.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(goal)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(goal)
        self.lbl_title.setMinimumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(goal)
        self.groupBox.setMinimumSize(QtCore.QSize(741, 331))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lbl_targetWeight = QtWidgets.QLabel(self.groupBox)
        self.lbl_targetWeight.setMinimumSize(QtCore.QSize(221, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_targetWeight.setFont(font)
        self.lbl_targetWeight.setObjectName("lbl_targetWeight")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_targetWeight)
        self.lbl_targetWeightVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_targetWeightVal.setMinimumSize(QtCore.QSize(461, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_targetWeightVal.setFont(font)
        self.lbl_targetWeightVal.setObjectName("lbl_targetWeightVal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_targetWeightVal)
        self.lbl_recommendedWeight = QtWidgets.QLabel(self.groupBox)
        self.lbl_recommendedWeight.setMinimumSize(QtCore.QSize(221, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_recommendedWeight.setFont(font)
        self.lbl_recommendedWeight.setObjectName("lbl_recommendedWeight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_recommendedWeight)
        self.lbl_recommendedWeightVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_recommendedWeightVal.setMinimumSize(QtCore.QSize(461, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_recommendedWeightVal.setFont(font)
        self.lbl_recommendedWeightVal.setObjectName("lbl_recommendedWeightVal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_recommendedWeightVal)
        self.lbl_targetIntake = QtWidgets.QLabel(self.groupBox)
        self.lbl_targetIntake.setMinimumSize(QtCore.QSize(221, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_targetIntake.setFont(font)
        self.lbl_targetIntake.setObjectName("lbl_targetIntake")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_targetIntake)
        self.lbl_targetIntakeVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_targetIntakeVal.setMinimumSize(QtCore.QSize(461, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_targetIntakeVal.setFont(font)
        self.lbl_targetIntakeVal.setObjectName("lbl_targetIntakeVal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbl_targetIntakeVal)
        self.lbl_recommendedIntake = QtWidgets.QLabel(self.groupBox)
        self.lbl_recommendedIntake.setMinimumSize(QtCore.QSize(221, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_recommendedIntake.setFont(font)
        self.lbl_recommendedIntake.setObjectName("lbl_recommendedIntake")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_recommendedIntake)
        self.lbl_recommendedIntakeVal = QtWidgets.QLabel(self.groupBox)
        self.lbl_recommendedIntakeVal.setMinimumSize(QtCore.QSize(461, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.lbl_recommendedIntakeVal.setFont(font)
        self.lbl_recommendedIntakeVal.setObjectName("lbl_recommendedIntakeVal")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lbl_recommendedIntakeVal)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.btn_back = QtWidgets.QPushButton(goal)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(487, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btn_edit = QtWidgets.QPushButton(goal)
        self.btn_edit.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")
        self.gridLayout.addWidget(self.btn_edit, 2, 2, 1, 1)

        self.retranslateUi(goal)
        QtCore.QMetaObject.connectSlotsByName(goal)

    def retranslateUi(self, goal):
        _translate = QtCore.QCoreApplication.translate
        goal.setWindowTitle(_translate("goal", "goal"))
        self.lbl_title.setText(_translate("goal", "Goal"))
        self.lbl_targetWeight.setText(_translate("goal", "Taget Weight:"))
        self.lbl_targetWeightVal.setText(_translate("goal", "Target Weight"))
        self.lbl_recommendedWeight.setText(_translate("goal", "Recommended Weight:"))
        self.lbl_recommendedWeightVal.setText(_translate("goal", "Recommended Weight"))
        self.lbl_targetIntake.setText(_translate("goal", "Target Intake:"))
        self.lbl_targetIntakeVal.setText(_translate("goal", "Target Intake"))
        self.lbl_recommendedIntake.setText(_translate("goal", "Recommended Intake:"))
        self.lbl_recommendedIntakeVal.setText(_translate("goal", "Recommended Intake"))
        self.btn_back.setText(_translate("goal", "Back"))
        self.btn_edit.setText(_translate("goal", "Edit"))

