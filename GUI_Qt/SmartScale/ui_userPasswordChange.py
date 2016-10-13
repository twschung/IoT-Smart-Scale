# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userPasswordChange.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userPasswordChange(object):
    def setupUi(self, userPasswordChange):
        userPasswordChange.setObjectName("userPasswordChange")
        userPasswordChange.resize(1024, 600)
        self.centralWidget = QtWidgets.QWidget(userPasswordChange)
        self.centralWidget.setObjectName("centralWidget")
        self.btnChangePassword = QtWidgets.QPushButton(self.centralWidget)
        self.btnChangePassword.setGeometry(QtCore.QRect(780, 60, 221, 31))
        self.btnChangePassword.setObjectName("btnChangePassword")
        self.btnCancel = QtWidgets.QPushButton(self.centralWidget)
        self.btnCancel.setGeometry(QtCore.QRect(780, 100, 221, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.lblOldPassword = QtWidgets.QLabel(self.centralWidget)
        self.lblOldPassword.setGeometry(QtCore.QRect(20, 62, 71, 21))
        self.lblOldPassword.setObjectName("lblOldPassword")
        self.lblNewPassword = QtWidgets.QLabel(self.centralWidget)
        self.lblNewPassword.setGeometry(QtCore.QRect(20, 102, 81, 21))
        self.lblNewPassword.setObjectName("lblNewPassword")
        self.lblTitle = QtWidgets.QLabel(self.centralWidget)
        self.lblTitle.setGeometry(QtCore.QRect(20, 10, 201, 41))
        self.lblTitle.setObjectName("lblTitle")
        self.txtUsername = QtWidgets.QLineEdit(self.centralWidget)
        self.txtUsername.setGeometry(QtCore.QRect(130, 60, 621, 31))
        self.txtUsername.setObjectName("txtUsername")
        self.txtNewPassword = QtWidgets.QLineEdit(self.centralWidget)
        self.txtNewPassword.setGeometry(QtCore.QRect(130, 100, 621, 31))
        self.txtNewPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtNewPassword.setInputMask("")
        self.txtNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPassword.setObjectName("txtNewPassword")
        self.lblStatus = QtWidgets.QLabel(self.centralWidget)
        self.lblStatus.setGeometry(QtCore.QRect(190, 10, 711, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.txtComfirmPassword = QtWidgets.QLineEdit(self.centralWidget)
        self.txtComfirmPassword.setGeometry(QtCore.QRect(130, 138, 621, 31))
        self.txtComfirmPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtComfirmPassword.setInputMask("")
        self.txtComfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtComfirmPassword.setObjectName("txtComfirmPassword")
        self.lblComfirmPassword = QtWidgets.QLabel(self.centralWidget)
        self.lblComfirmPassword.setGeometry(QtCore.QRect(20, 140, 111, 21))
        self.lblComfirmPassword.setObjectName("lblComfirmPassword")
        userPasswordChange.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(userPasswordChange)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName("menuBar")
        userPasswordChange.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(userPasswordChange)
        self.mainToolBar.setObjectName("mainToolBar")
        userPasswordChange.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(userPasswordChange)
        self.statusBar.setObjectName("statusBar")
        userPasswordChange.setStatusBar(self.statusBar)

        self.retranslateUi(userPasswordChange)
        QtCore.QMetaObject.connectSlotsByName(userPasswordChange)

    def retranslateUi(self, userPasswordChange):
        _translate = QtCore.QCoreApplication.translate
        userPasswordChange.setWindowTitle(_translate("userPasswordChange", "smartScaleGUI"))
        self.btnChangePassword.setText(_translate("userPasswordChange", "Change Password"))
        self.btnCancel.setText(_translate("userPasswordChange", "Cancel"))
        self.lblOldPassword.setText(_translate("userPasswordChange", "Old Passwod :"))
        self.lblNewPassword.setText(_translate("userPasswordChange", "New Password :"))
        self.lblTitle.setText(_translate("userPasswordChange", "Please enter the following :"))
        self.lblComfirmPassword.setText(_translate("userPasswordChange", "Comfirm Password :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userPasswordChange = QtWidgets.QMainWindow()
    ui = Ui_userPasswordChange()
    ui.setupUi(userPasswordChange)
    userPasswordChange.show()
    sys.exit(app.exec_())

