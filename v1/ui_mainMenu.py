# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(1024, 565)
        self.centralWidget = QtWidgets.QWidget(mainMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.lblStatus = QtWidgets.QLabel(self.centralWidget)
        self.lblStatus.setGeometry(QtCore.QRect(20, 10, 961, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.btnChangePassword = QtWidgets.QPushButton(self.centralWidget)
        self.btnChangePassword.setGeometry(QtCore.QRect(20, 300, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnChangePassword.setFont(font)
        self.btnChangePassword.setObjectName("btnChangePassword")
        self.btnChangeUserDetail = QtWidgets.QPushButton(self.centralWidget)
        self.btnChangeUserDetail.setGeometry(QtCore.QRect(350, 300, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnChangeUserDetail.setFont(font)
        self.btnChangeUserDetail.setObjectName("btnChangeUserDetail")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 70, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 70, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 70, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.btnLogout = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogout.setGeometry(QtCore.QRect(680, 300, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLogout.setFont(font)
        self.btnLogout.setObjectName("btnLogout")
        mainMenu.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainMenu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName("menuBar")
        mainMenu.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(mainMenu)
        self.mainToolBar.setObjectName("mainToolBar")
        mainMenu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(mainMenu)
        self.statusBar.setObjectName("statusBar")
        mainMenu.setStatusBar(self.statusBar)

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "smartScaleGUI"))
        self.btnChangePassword.setText(_translate("mainMenu", "Change Password"))
        self.btnChangeUserDetail.setText(_translate("mainMenu", "Change User Detail"))
        self.pushButton_3.setText(_translate("mainMenu", "/"))
        self.pushButton_4.setText(_translate("mainMenu", "/"))
        self.pushButton_5.setText(_translate("mainMenu", "/"))
        self.btnLogout.setText(_translate("mainMenu", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())

