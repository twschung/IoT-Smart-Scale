# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newLogin.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newLogin(object):
    def setupUi(self, newLogin):
        newLogin.setObjectName("newLogin")
        newLogin.resize(800, 480)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        newLogin.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(newLogin)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_login = QtWidgets.QPushButton(newLogin)
        self.btn_login.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.gridLayout.addWidget(self.btn_login, 2, 2, 1, 1)
        self.btn_back = QtWidgets.QPushButton(newLogin)
        self.btn_back.setMinimumSize(QtCore.QSize(141, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        self.lbl_title = QtWidgets.QLabel(newLogin)
        self.lbl_title.setMinimumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(487, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(newLogin)
        self.groupBox.setMinimumSize(QtCore.QSize(741, 331))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lbl_email = QtWidgets.QLabel(self.groupBox)
        self.lbl_email.setGeometry(QtCore.QRect(15, 15, 50, 20))
        self.lbl_email.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_email.setFont(font)
        self.lbl_email.setObjectName("lbl_email")
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setGeometry(QtCore.QRect(73, 15, 513, 21))
        self.lineEdit_email.setMinimumSize(QtCore.QSize(513, 19))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.keyboard = QtWidgets.QFrame(self.groupBox)
        self.keyboard.setGeometry(QtCore.QRect(70, 60, 561, 241))
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row1.addItem(spacerItem1)
        self.Q = QtWidgets.QPushButton(self.keyboard)
        self.Q.setMinimumSize(QtCore.QSize(46, 46))
        self.Q.setObjectName("Q")
        self.row1.addWidget(self.Q)
        self.W = QtWidgets.QPushButton(self.keyboard)
        self.W.setMinimumSize(QtCore.QSize(46, 46))
        self.W.setObjectName("W")
        self.row1.addWidget(self.W)
        self.E = QtWidgets.QPushButton(self.keyboard)
        self.E.setMinimumSize(QtCore.QSize(46, 46))
        self.E.setObjectName("E")
        self.row1.addWidget(self.E)
        self.R = QtWidgets.QPushButton(self.keyboard)
        self.R.setMinimumSize(QtCore.QSize(46, 46))
        self.R.setObjectName("R")
        self.row1.addWidget(self.R)
        self.T = QtWidgets.QPushButton(self.keyboard)
        self.T.setMinimumSize(QtCore.QSize(46, 46))
        self.T.setObjectName("T")
        self.row1.addWidget(self.T)
        self.Y = QtWidgets.QPushButton(self.keyboard)
        self.Y.setMinimumSize(QtCore.QSize(46, 46))
        self.Y.setObjectName("Y")
        self.row1.addWidget(self.Y)
        self.U = QtWidgets.QPushButton(self.keyboard)
        self.U.setMinimumSize(QtCore.QSize(46, 46))
        self.U.setObjectName("U")
        self.row1.addWidget(self.U)
        self.I = QtWidgets.QPushButton(self.keyboard)
        self.I.setMinimumSize(QtCore.QSize(46, 46))
        self.I.setObjectName("I")
        self.row1.addWidget(self.I)
        self.O = QtWidgets.QPushButton(self.keyboard)
        self.O.setMinimumSize(QtCore.QSize(46, 46))
        self.O.setObjectName("O")
        self.row1.addWidget(self.O)
        self.P = QtWidgets.QPushButton(self.keyboard)
        self.P.setMinimumSize(QtCore.QSize(46, 46))
        self.P.setObjectName("P")
        self.row1.addWidget(self.P)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row1.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.row1)
        self.row2 = QtWidgets.QHBoxLayout()
        self.row2.setContentsMargins(11, 11, 11, 11)
        self.row2.setSpacing(6)
        self.row2.setObjectName("row2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row2.addItem(spacerItem3)
        self.A = QtWidgets.QPushButton(self.keyboard)
        self.A.setMinimumSize(QtCore.QSize(46, 46))
        self.A.setObjectName("A")
        self.row2.addWidget(self.A)
        self.S = QtWidgets.QPushButton(self.keyboard)
        self.S.setMinimumSize(QtCore.QSize(46, 46))
        self.S.setObjectName("S")
        self.row2.addWidget(self.S)
        self.D = QtWidgets.QPushButton(self.keyboard)
        self.D.setMinimumSize(QtCore.QSize(46, 46))
        self.D.setObjectName("D")
        self.row2.addWidget(self.D)
        self.F = QtWidgets.QPushButton(self.keyboard)
        self.F.setMinimumSize(QtCore.QSize(46, 46))
        self.F.setObjectName("F")
        self.row2.addWidget(self.F)
        self.G = QtWidgets.QPushButton(self.keyboard)
        self.G.setMinimumSize(QtCore.QSize(46, 46))
        self.G.setObjectName("G")
        self.row2.addWidget(self.G)
        self.H = QtWidgets.QPushButton(self.keyboard)
        self.H.setMinimumSize(QtCore.QSize(46, 46))
        self.H.setObjectName("H")
        self.row2.addWidget(self.H)
        self.J = QtWidgets.QPushButton(self.keyboard)
        self.J.setMinimumSize(QtCore.QSize(46, 46))
        self.J.setObjectName("J")
        self.row2.addWidget(self.J)
        self.K = QtWidgets.QPushButton(self.keyboard)
        self.K.setMinimumSize(QtCore.QSize(46, 46))
        self.K.setObjectName("K")
        self.row2.addWidget(self.K)
        self.L = QtWidgets.QPushButton(self.keyboard)
        self.L.setMinimumSize(QtCore.QSize(46, 46))
        self.L.setObjectName("L")
        self.row2.addWidget(self.L)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.row2)
        self.row3 = QtWidgets.QHBoxLayout()
        self.row3.setContentsMargins(11, 11, 11, 11)
        self.row3.setSpacing(6)
        self.row3.setObjectName("row3")
        self.btnShift = QtWidgets.QPushButton(self.keyboard)
        self.btnShift.setMinimumSize(QtCore.QSize(0, 46))
        self.btnShift.setObjectName("btnShift")
        self.row3.addWidget(self.btnShift)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row3.addItem(spacerItem5)
        self.Z = QtWidgets.QPushButton(self.keyboard)
        self.Z.setMinimumSize(QtCore.QSize(46, 46))
        self.Z.setObjectName("Z")
        self.row3.addWidget(self.Z)
        self.X = QtWidgets.QPushButton(self.keyboard)
        self.X.setMinimumSize(QtCore.QSize(46, 46))
        self.X.setObjectName("X")
        self.row3.addWidget(self.X)
        self.C = QtWidgets.QPushButton(self.keyboard)
        self.C.setMinimumSize(QtCore.QSize(46, 46))
        self.C.setObjectName("C")
        self.row3.addWidget(self.C)
        self.V = QtWidgets.QPushButton(self.keyboard)
        self.V.setMinimumSize(QtCore.QSize(46, 46))
        self.V.setObjectName("V")
        self.row3.addWidget(self.V)
        self.B = QtWidgets.QPushButton(self.keyboard)
        self.B.setMinimumSize(QtCore.QSize(46, 46))
        self.B.setObjectName("B")
        self.row3.addWidget(self.B)
        self.N = QtWidgets.QPushButton(self.keyboard)
        self.N.setMinimumSize(QtCore.QSize(46, 46))
        self.N.setObjectName("N")
        self.row3.addWidget(self.N)
        self.M = QtWidgets.QPushButton(self.keyboard)
        self.M.setMinimumSize(QtCore.QSize(46, 46))
        self.M.setObjectName("M")
        self.row3.addWidget(self.M)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row3.addItem(spacerItem6)
        self.btnDel = QtWidgets.QPushButton(self.keyboard)
        self.btnDel.setMinimumSize(QtCore.QSize(0, 46))
        self.btnDel.setObjectName("btnDel")
        self.row3.addWidget(self.btnDel)
        self.verticalLayout.addLayout(self.row3)
        self.row4 = QtWidgets.QHBoxLayout()
        self.row4.setContentsMargins(11, 11, 11, 11)
        self.row4.setSpacing(6)
        self.row4.setObjectName("row4")
        self.btnToggle = QtWidgets.QPushButton(self.keyboard)
        self.btnToggle.setMinimumSize(QtCore.QSize(0, 46))
        self.btnToggle.setObjectName("btnToggle")
        self.row4.addWidget(self.btnToggle)
        spacerItem7 = QtWidgets.QSpacerItem(0, 46, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row4.addItem(spacerItem7)
        self.space = QtWidgets.QPushButton(self.keyboard)
        self.space.setMinimumSize(QtCore.QSize(221, 46))
        self.space.setObjectName("space")
        self.row4.addWidget(self.space)
        self.btnAt = QtWidgets.QPushButton(self.keyboard)
        self.btnAt.setMinimumSize(QtCore.QSize(46, 46))
        self.btnAt.setObjectName("btnAt")
        self.row4.addWidget(self.btnAt)
        self.btnDot = QtWidgets.QPushButton(self.keyboard)
        self.btnDot.setMinimumSize(QtCore.QSize(46, 46))
        self.btnDot.setObjectName("btnDot")
        self.row4.addWidget(self.btnDot)
        self.btnReturn = QtWidgets.QPushButton(self.keyboard)
        self.btnReturn.setMinimumSize(QtCore.QSize(0, 46))
        self.btnReturn.setObjectName("btnReturn")
        self.row4.addWidget(self.btnReturn)
        self.verticalLayout.addLayout(self.row4)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)

        self.retranslateUi(newLogin)
        QtCore.QMetaObject.connectSlotsByName(newLogin)

    def retranslateUi(self, newLogin):
        _translate = QtCore.QCoreApplication.translate
        newLogin.setWindowTitle(_translate("newLogin", "newLogin"))
        self.btn_login.setText(_translate("newLogin", "Login"))
        self.btn_back.setText(_translate("newLogin", "Back"))
        self.lbl_title.setText(_translate("newLogin", "New Login"))
        self.lbl_email.setText(_translate("newLogin", "Email:"))
        self.Q.setText(_translate("newLogin", "Q"))
        self.W.setText(_translate("newLogin", "W"))
        self.E.setText(_translate("newLogin", "E"))
        self.R.setText(_translate("newLogin", "R"))
        self.T.setText(_translate("newLogin", "T"))
        self.Y.setText(_translate("newLogin", "Y"))
        self.U.setText(_translate("newLogin", "U"))
        self.I.setText(_translate("newLogin", "I"))
        self.O.setText(_translate("newLogin", "O"))
        self.P.setText(_translate("newLogin", "P"))
        self.A.setText(_translate("newLogin", "A"))
        self.S.setText(_translate("newLogin", "S"))
        self.D.setText(_translate("newLogin", "D"))
        self.F.setText(_translate("newLogin", "F"))
        self.G.setText(_translate("newLogin", "G"))
        self.H.setText(_translate("newLogin", "H"))
        self.J.setText(_translate("newLogin", "J"))
        self.K.setText(_translate("newLogin", "K"))
        self.L.setText(_translate("newLogin", "L"))
        self.btnShift.setText(_translate("newLogin", "Shift"))
        self.Z.setText(_translate("newLogin", "Z"))
        self.X.setText(_translate("newLogin", "X"))
        self.C.setText(_translate("newLogin", "C"))
        self.V.setText(_translate("newLogin", "V"))
        self.B.setText(_translate("newLogin", "B"))
        self.N.setText(_translate("newLogin", "N"))
        self.M.setText(_translate("newLogin", "M"))
        self.btnDel.setText(_translate("newLogin", "Del"))
        self.btnToggle.setText(_translate("newLogin", "123"))
        self.space.setText(_translate("newLogin", "space"))
        self.btnAt.setText(_translate("newLogin", "@"))
        self.btnDot.setText(_translate("newLogin", "."))
        self.btnReturn.setText(_translate("newLogin", "return"))

