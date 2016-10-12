# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1024, 600)
        self.centralWidget = QtWidgets.QWidget(login)
        self.centralWidget.setObjectName("centralWidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogin.setGeometry(QtCore.QRect(780, 60, 221, 31))
        self.btnLogin.setObjectName("btnLogin")
        self.btnRegister = QtWidgets.QPushButton(self.centralWidget)
        self.btnRegister.setGeometry(QtCore.QRect(780, 110, 221, 31))
        self.btnRegister.setObjectName("btnRegister")
        self.lblUsername = QtWidgets.QLabel(self.centralWidget)
        self.lblUsername.setGeometry(QtCore.QRect(20, 62, 71, 21))
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtWidgets.QLabel(self.centralWidget)
        self.lblPassword.setGeometry(QtCore.QRect(20, 112, 81, 21))
        self.lblPassword.setObjectName("lblPassword")
        self.lblTitle = QtWidgets.QLabel(self.centralWidget)
        self.lblTitle.setGeometry(QtCore.QRect(20, 10, 201, 41))
        self.lblTitle.setObjectName("lblTitle")
        self.txtUsername = QtWidgets.QLineEdit(self.centralWidget)
        self.txtUsername.setGeometry(QtCore.QRect(110, 60, 641, 31))
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(self.centralWidget)
        self.txtPassword.setGeometry(QtCore.QRect(110, 110, 641, 31))
        self.txtPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtPassword.setInputMask("")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.lblStatus = QtWidgets.QLabel(self.centralWidget)
        self.lblStatus.setGeometry(QtCore.QRect(270, 10, 711, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        login.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(login)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName("menuBar")
        login.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(login)
        self.mainToolBar.setObjectName("mainToolBar")
        login.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(login)
        self.statusBar.setObjectName("statusBar")
        login.setStatusBar(self.statusBar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "smartScaleGUI"))
        self.btnLogin.setText(_translate("login", "Login"))
        self.btnRegister.setText(_translate("login", "New User Register"))
        self.lblUsername.setText(_translate("login", "Username :"))
        self.lblPassword.setText(_translate("login", "Password :"))
        self.lblTitle.setText(_translate("login", "Please enter Username and Password : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

