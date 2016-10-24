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
        userPasswordChange.resize(1024, 565)
        self.centralWidget = QtWidgets.QWidget(userPasswordChange)
        self.centralWidget.setObjectName("centralWidget")
        self.btnChangePassword = QtWidgets.QPushButton(self.centralWidget)
        self.btnChangePassword.setGeometry(QtCore.QRect(780, 60, 221, 31))
        self.btnChangePassword.setObjectName("btnChangePassword")
        self.btnCancel = QtWidgets.QPushButton(self.centralWidget)
        self.btnCancel.setGeometry(QtCore.QRect(780, 100, 221, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.lblTitle = QtWidgets.QLabel(self.centralWidget)
        self.lblTitle.setGeometry(QtCore.QRect(20, 10, 201, 41))
        self.lblTitle.setObjectName("lblTitle")
        self.lblStatus = QtWidgets.QLabel(self.centralWidget)
        self.lblStatus.setGeometry(QtCore.QRect(210, 10, 711, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 741, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lblOldPassword = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblOldPassword.setObjectName("lblOldPassword")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblOldPassword)
        self.txtOldPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtOldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtOldPassword.setObjectName("txtOldPassword")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtOldPassword)
        self.lblNewPassword = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblNewPassword.setObjectName("lblNewPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblNewPassword)
        self.txtNewPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNewPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtNewPassword.setInputMask("")
        self.txtNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPassword.setObjectName("txtNewPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNewPassword)
        self.lblComfirmPassword = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblComfirmPassword.setObjectName("lblComfirmPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblComfirmPassword)
        self.txtConfirmPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtConfirmPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtConfirmPassword.setInputMask("")
        self.txtConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtConfirmPassword)
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
        self.lblTitle.setText(_translate("userPasswordChange", "Please enter the following :"))
        self.lblOldPassword.setText(_translate("userPasswordChange", "Old Passwod :"))
        self.lblNewPassword.setText(_translate("userPasswordChange", "New Password :"))
        self.lblComfirmPassword.setText(_translate("userPasswordChange", "Comfirm Password :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userPasswordChange = QtWidgets.QMainWindow()
    ui = Ui_userPasswordChange()
    ui.setupUi(userPasswordChange)
    userPasswordChange.show()
    sys.exit(app.exec_())

