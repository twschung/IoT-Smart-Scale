# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userRegister.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userRegister(object):
    def setupUi(self, userRegister):
        userRegister.setObjectName("userRegister")
        userRegister.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(userRegister)
        self.centralWidget.setObjectName("centralWidget")
        self.btnCancel = QtWidgets.QPushButton(self.centralWidget)
        self.btnCancel.setGeometry(QtCore.QRect(570, 100, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.btnRegister = QtWidgets.QPushButton(self.centralWidget)
        self.btnRegister.setGeometry(QtCore.QRect(570, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnRegister.setFont(font)
        self.btnRegister.setObjectName("btnRegister")
        self.lblTitle = QtWidgets.QLabel(self.centralWidget)
        self.lblTitle.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblStatus = QtWidgets.QLabel(self.centralWidget)
        self.lblStatus.setGeometry(QtCore.QRect(250, 10, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 551, 341))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lblUsername = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblUsername)
        self.txtUsername = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUsername)
        self.lblPassword = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblPassword)
        self.txtPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtPassword.setFont(font)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPassword)
        self.lblConfirmPassword = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblConfirmPassword.setFont(font)
        self.lblConfirmPassword.setObjectName("lblConfirmPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblConfirmPassword)
        self.txtConfirmPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtConfirmPassword.setFont(font)
        self.txtConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtConfirmPassword)
        self.lblEmail = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblEmail)
        self.txtEmail = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtEmail)
        self.lblFirstname = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblFirstname.setFont(font)
        self.lblFirstname.setObjectName("lblFirstname")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblFirstname)
        self.txtFirstname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtFirstname.setFont(font)
        self.txtFirstname.setObjectName("txtFirstname")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtFirstname)
        self.lblLastname = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblLastname.setFont(font)
        self.lblLastname.setObjectName("lblLastname")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblLastname)
        self.txtLastname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtLastname.setFont(font)
        self.txtLastname.setObjectName("txtLastname")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtLastname)
        self.lblDoB = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblDoB.setFont(font)
        self.lblDoB.setObjectName("lblDoB")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblDoB)
        self.datDoB = QtWidgets.QDateEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.datDoB.setFont(font)
        self.datDoB.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.datDoB.setCalendarPopup(True)
        self.datDoB.setObjectName("datDoB")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.datDoB)
        self.lblGender = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblGender.setFont(font)
        self.lblGender.setObjectName("lblGender")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lblGender)
        self.rbnMale = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.rbnMale.setFont(font)
        self.rbnMale.setObjectName("rbnMale")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.rbnMale)
        self.lblHeight = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblHeight.setFont(font)
        self.lblHeight.setObjectName("lblHeight")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lblHeight)
        self.txtHeight = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtHeight.setFont(font)
        self.txtHeight.setObjectName("txtHeight")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.txtHeight)
        self.lblWeight = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lblWeight.setFont(font)
        self.lblWeight.setObjectName("lblWeight")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lblWeight)
        self.txtWeight = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.txtWeight.setFont(font)
        self.txtWeight.setObjectName("txtWeight")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.txtWeight)
        self.rbnFemale = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.rbnFemale.setFont(font)
        self.rbnFemale.setObjectName("rbnFemale")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.rbnFemale)
        userRegister.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(userRegister)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        userRegister.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(userRegister)
        self.mainToolBar.setObjectName("mainToolBar")
        userRegister.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(userRegister)
        self.statusBar.setObjectName("statusBar")
        userRegister.setStatusBar(self.statusBar)

        self.retranslateUi(userRegister)
        QtCore.QMetaObject.connectSlotsByName(userRegister)

    def retranslateUi(self, userRegister):
        _translate = QtCore.QCoreApplication.translate
        userRegister.setWindowTitle(_translate("userRegister", "smartScaleGUI"))
        self.btnCancel.setText(_translate("userRegister", "Cancel"))
        self.btnRegister.setText(_translate("userRegister", "Register"))
        self.lblTitle.setText(_translate("userRegister", "<html><head/><body><p>Please enter the following details :</p></body></html>"))
        self.lblUsername.setText(_translate("userRegister", "Username :"))
        self.lblPassword.setText(_translate("userRegister", "Password :"))
        self.lblConfirmPassword.setText(_translate("userRegister", "Confirm Password :"))
        self.lblEmail.setText(_translate("userRegister", "Email :"))
        self.lblFirstname.setText(_translate("userRegister", "Firstname :"))
        self.lblLastname.setText(_translate("userRegister", "Lastname :"))
        self.lblDoB.setText(_translate("userRegister", "Date of Birth :"))
        self.datDoB.setDisplayFormat(_translate("userRegister", "dd-MMM-yyyy"))
        self.lblGender.setText(_translate("userRegister", "Gender :"))
        self.rbnMale.setText(_translate("userRegister", "Male"))
        self.lblHeight.setText(_translate("userRegister", "Height (cm) :"))
        self.lblWeight.setText(_translate("userRegister", "Weight (kg) :"))
        self.rbnFemale.setText(_translate("userRegister", "Female"))
