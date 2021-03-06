# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numInput.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_numInput(object):
    def setupUi(self, numInput):
        numInput.setObjectName("numInput")
        numInput.resize(800, 480)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        numInput.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(numInput)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_next = QtWidgets.QPushButton(numInput)
        self.btn_next.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_next.setFont(font)
        self.btn_next.setObjectName("btn_next")
        self.gridLayout.addWidget(self.btn_next, 2, 2, 1, 1)
        self.btn_back = QtWidgets.QPushButton(numInput)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(487, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(numInput)
        self.groupBox.setMinimumSize(QtCore.QSize(741, 331))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lbl_currentText = QtWidgets.QLabel(self.groupBox)
        self.lbl_currentText.setGeometry(QtCore.QRect(15, 15, 141, 20))
        self.lbl_currentText.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currentText.setFont(font)
        self.lbl_currentText.setText("")
        self.lbl_currentText.setObjectName("lbl_currentText")
        self.lineEdit_currentText = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_currentText.setGeometry(QtCore.QRect(163, 5, 591, 41))
        self.lineEdit_currentText.setMinimumSize(QtCore.QSize(513, 19))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_currentText.setFont(font)
        self.lineEdit_currentText.setObjectName("lineEdit_currentText")
        self.keyboard = QtWidgets.QFrame(self.groupBox)
        self.keyboard.setGeometry(QtCore.QRect(130, 50, 511, 281))
        self.keyboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keyboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keyboard.setObjectName("keyboard")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.keyboard)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.row1 = QtWidgets.QHBoxLayout()
        self.row1.setContentsMargins(11, 11, 11, 11)
        self.row1.setSpacing(6)
        self.row1.setObjectName("row1")
        self.btn_1 = QtWidgets.QPushButton(self.keyboard)
        self.btn_1.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_1.setObjectName("btn_1")
        self.row1.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.keyboard)
        self.btn_2.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_2.setObjectName("btn_2")
        self.row1.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.keyboard)
        self.btn_3.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_3.setObjectName("btn_3")
        self.row1.addWidget(self.btn_3)
        self.verticalLayout.addLayout(self.row1)
        self.row2 = QtWidgets.QHBoxLayout()
        self.row2.setContentsMargins(11, 11, 11, 11)
        self.row2.setSpacing(6)
        self.row2.setObjectName("row2")
        self.btn_4 = QtWidgets.QPushButton(self.keyboard)
        self.btn_4.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_4.setObjectName("btn_4")
        self.row2.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.keyboard)
        self.btn_5.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_5.setObjectName("btn_5")
        self.row2.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.keyboard)
        self.btn_6.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_6.setObjectName("btn_6")
        self.row2.addWidget(self.btn_6)
        self.verticalLayout.addLayout(self.row2)
        self.row3 = QtWidgets.QHBoxLayout()
        self.row3.setContentsMargins(11, 11, 11, 11)
        self.row3.setSpacing(6)
        self.row3.setObjectName("row3")
        self.btn_7 = QtWidgets.QPushButton(self.keyboard)
        self.btn_7.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_7.setObjectName("btn_7")
        self.row3.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.keyboard)
        self.btn_8.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_8.setObjectName("btn_8")
        self.row3.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.keyboard)
        self.btn_9.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_9.setObjectName("btn_9")
        self.row3.addWidget(self.btn_9)
        self.verticalLayout.addLayout(self.row3)
        self.row4 = QtWidgets.QHBoxLayout()
        self.row4.setContentsMargins(11, 11, 11, 11)
        self.row4.setSpacing(6)
        self.row4.setObjectName("row4")
        self.btn_dot = QtWidgets.QPushButton(self.keyboard)
        self.btn_dot.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_dot.setObjectName("btn_dot")
        self.row4.addWidget(self.btn_dot)
        self.btn_0 = QtWidgets.QPushButton(self.keyboard)
        self.btn_0.setMinimumSize(QtCore.QSize(46, 55))
        self.btn_0.setObjectName("btn_0")
        self.row4.addWidget(self.btn_0)
        self.btn_del = QtWidgets.QPushButton(self.keyboard)
        self.btn_del.setMinimumSize(QtCore.QSize(100, 55))
        self.btn_del.setObjectName("btn_del")
        self.row4.addWidget(self.btn_del)
        self.verticalLayout.addLayout(self.row4)
        self.btn_unit = QtWidgets.QPushButton(self.groupBox)
        self.btn_unit.setGeometry(QtCore.QRect(640, 260, 141, 71))
        self.btn_unit.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_unit.setFont(font)
        self.btn_unit.setText("")
        self.btn_unit.setObjectName("btn_unit")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.lbl_title = QtWidgets.QLabel(numInput)
        self.lbl_title.setMinimumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 3)

        self.retranslateUi(numInput)
        QtCore.QMetaObject.connectSlotsByName(numInput)

    def retranslateUi(self, numInput):
        _translate = QtCore.QCoreApplication.translate
        numInput.setWindowTitle(_translate("numInput", "newLogin"))
        self.btn_next.setText(_translate("numInput", "Next"))
        self.btn_back.setText(_translate("numInput", "Back"))
        self.btn_1.setText(_translate("numInput", "1"))
        self.btn_2.setText(_translate("numInput", "2"))
        self.btn_3.setText(_translate("numInput", "3"))
        self.btn_4.setText(_translate("numInput", "4"))
        self.btn_5.setText(_translate("numInput", "5"))
        self.btn_6.setText(_translate("numInput", "6"))
        self.btn_7.setText(_translate("numInput", "7"))
        self.btn_8.setText(_translate("numInput", "8"))
        self.btn_9.setText(_translate("numInput", "9"))
        self.btn_dot.setText(_translate("numInput", "."))
        self.btn_0.setText(_translate("numInput", "0"))
        self.btn_del.setText(_translate("numInput", "DEL"))
        self.lbl_title.setText(_translate("numInput", "-"))

