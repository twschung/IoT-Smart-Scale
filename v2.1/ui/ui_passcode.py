# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passcode.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_passCode(object):
    def setupUi(self, passCode):
        passCode.setObjectName("passCode")
        passCode.resize(875, 480)
        self.gridLayout = QtWidgets.QGridLayout(passCode)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(passCode)
        self.lbl_title.setMinimumSize(QtCore.QSize(201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        self.lbl_info = QtWidgets.QLabel(passCode)
        self.lbl_info.setObjectName("lbl_info")
        self.verticalLayout.addWidget(self.lbl_info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(43, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_1 = QtWidgets.QLineEdit(passCode)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout.addWidget(self.lineEdit_1)
        spacerItem1 = QtWidgets.QSpacerItem(43, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEdit_2 = QtWidgets.QLineEdit(passCode)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(43, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_3 = QtWidgets.QLineEdit(passCode)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        spacerItem3 = QtWidgets.QSpacerItem(43, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lineEdit_4 = QtWidgets.QLineEdit(passCode)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        spacerItem4 = QtWidgets.QSpacerItem(43, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(passCode)
        self.frame.setMinimumSize(QtCore.QSize(450, 240))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_blank = QtWidgets.QPushButton(self.frame)
        self.btn_blank.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_blank.sizePolicy().hasHeightForWidth())
        self.btn_blank.setSizePolicy(sizePolicy)
        self.btn_blank.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_blank.setFont(font)
        self.btn_blank.setText("")
        self.btn_blank.setObjectName("btn_blank")
        self.gridLayout_2.addWidget(self.btn_blank, 3, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_2.addWidget(self.btn_0, 3, 1, 1, 1)
        self.btn_del = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.gridLayout_2.addWidget(self.btn_del, 3, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 2, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 0, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 2, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 0, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_forgot = QtWidgets.QPushButton(passCode)
        self.btn_forgot.setMinimumSize(QtCore.QSize(121, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.btn_forgot.setFont(font)
        self.btn_forgot.setObjectName("btn_forgot")
        self.verticalLayout_2.addWidget(self.btn_forgot)
        self.btn_done = QtWidgets.QPushButton(passCode)
        self.btn_done.setMinimumSize(QtCore.QSize(121, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_done.setFont(font)
        self.btn_done.setObjectName("btn_done")
        self.verticalLayout_2.addWidget(self.btn_done)
        self.btn_back = QtWidgets.QPushButton(passCode)
        self.btn_back.setMinimumSize(QtCore.QSize(121, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.verticalLayout_2.addWidget(self.btn_back)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 6, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_remUser = QtWidgets.QPushButton(passCode)
        self.btn_remUser.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_remUser.setCheckable(True)
        self.btn_remUser.setObjectName("btn_remUser")
        self.verticalLayout_3.addWidget(self.btn_remUser)
        self.btn_remFingerPrint = QtWidgets.QPushButton(passCode)
        self.btn_remFingerPrint.setEnabled(False)
        self.btn_remFingerPrint.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_remFingerPrint.setCheckable(True)
        self.btn_remFingerPrint.setObjectName("btn_remFingerPrint")
        self.verticalLayout_3.addWidget(self.btn_remFingerPrint)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 6, 1, 1)

        self.retranslateUi(passCode)
        QtCore.QMetaObject.connectSlotsByName(passCode)

    def retranslateUi(self, passCode):
        _translate = QtCore.QCoreApplication.translate
        passCode.setWindowTitle(_translate("passCode", "passCode"))
        self.lbl_title.setText(_translate("passCode", "Passcode"))
        self.lbl_info.setText(_translate("passCode", "TextLabel"))
        self.btn_4.setText(_translate("passCode", "4"))
        self.btn_0.setText(_translate("passCode", "0"))
        self.btn_del.setText(_translate("passCode", "Del"))
        self.btn_8.setText(_translate("passCode", "8"))
        self.btn_9.setText(_translate("passCode", "9"))
        self.btn_2.setText(_translate("passCode", "2"))
        self.btn_6.setText(_translate("passCode", "6"))
        self.btn_7.setText(_translate("passCode", "7"))
        self.btn_3.setText(_translate("passCode", "3"))
        self.btn_5.setText(_translate("passCode", "5"))
        self.btn_1.setText(_translate("passCode", "1"))
        self.btn_forgot.setText(_translate("passCode", "Forgot"))
        self.btn_done.setText(_translate("passCode", "Done"))
        self.btn_back.setText(_translate("passCode", "Back"))
        self.btn_remUser.setText(_translate("passCode", "Remember\n"
"User"))
        self.btn_remFingerPrint.setText(_translate("passCode", "Remember\n"
"Finger\n"
"Print"))

