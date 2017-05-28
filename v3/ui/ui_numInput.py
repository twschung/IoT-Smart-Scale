# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numInput.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_numInput(object):
    def setupUi(self, numInput):
        numInput.setObjectName("numInput")
        numInput.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(11)
        numInput.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(numInput)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_back = QtWidgets.QPushButton(numInput)
        self.btn_back.setMinimumSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        self.lbl_title = QtWidgets.QLabel(numInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(numInput)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.keyboard = QtWidgets.QFrame(self.groupBox)
        self.keyboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keyboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keyboard.setObjectName("keyboard")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.keyboard)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_7 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_3.addWidget(self.btn_7, 2, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_3.addWidget(self.btn_8, 2, 3, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_3.addWidget(self.btn_9, 2, 4, 1, 1)
        self.btn_del = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_del.setObjectName("btn_del")
        self.gridLayout_3.addWidget(self.btn_del, 4, 4, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_3.addWidget(self.btn_6, 1, 4, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_3.addWidget(self.btn_5, 1, 3, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_3.addWidget(self.btn_0, 4, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_3.addWidget(self.btn_4, 1, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_3.addWidget(self.btn_3, 0, 4, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_3.addWidget(self.btn_1, 0, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_3.addWidget(self.btn_dot, 4, 2, 1, 1)
        self.btn_unit = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_unit.sizePolicy().hasHeightForWidth())
        self.btn_unit.setSizePolicy(sizePolicy)
        self.btn_unit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btn_unit.setText("")
        self.btn_unit.setObjectName("btn_unit")
        self.gridLayout_3.addWidget(self.btn_unit, 2, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_3.addWidget(self.btn_2, 0, 3, 1, 1)
        self.btn_next = QtWidgets.QPushButton(self.keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_next.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btn_next.setObjectName("btn_next")
        self.gridLayout_3.addWidget(self.btn_next, 4, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 7, 1, 1)
        self.gridLayout_2.addWidget(self.keyboard, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lbl_currentText = QtWidgets.QLabel(self.groupBox)
        self.lbl_currentText.setObjectName("lbl_currentText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_currentText)
        self.lineEdit_currentText = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_currentText.setText("")
        self.lineEdit_currentText.setObjectName("lineEdit_currentText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_currentText)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 4)

        self.retranslateUi(numInput)
        QtCore.QMetaObject.connectSlotsByName(numInput)

    def retranslateUi(self, numInput):
        _translate = QtCore.QCoreApplication.translate
        numInput.setWindowTitle(_translate("numInput", "newLogin"))
        self.btn_back.setText(_translate("numInput", "Back"))
        self.lbl_title.setText(_translate("numInput", "-"))
        self.btn_7.setText(_translate("numInput", "7"))
        self.btn_8.setText(_translate("numInput", "8"))
        self.btn_9.setText(_translate("numInput", "9"))
        self.btn_del.setText(_translate("numInput", "DEL"))
        self.btn_6.setText(_translate("numInput", "6"))
        self.btn_5.setText(_translate("numInput", "5"))
        self.btn_0.setText(_translate("numInput", "0"))
        self.btn_4.setText(_translate("numInput", "4"))
        self.btn_3.setText(_translate("numInput", "3"))
        self.btn_1.setText(_translate("numInput", "1"))
        self.btn_dot.setText(_translate("numInput", "."))
        self.btn_2.setText(_translate("numInput", "2"))
        self.btn_next.setText(_translate("numInput", "Next"))
        self.lbl_currentText.setText(_translate("numInput", "lbl_currentText"))

