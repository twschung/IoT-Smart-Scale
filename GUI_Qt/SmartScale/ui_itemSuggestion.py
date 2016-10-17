# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemSuggestion.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_itemSuggestion(object):
    def setupUi(self, itemSuggestion):
        itemSuggestion.setObjectName("itemSuggestion")
        itemSuggestion.resize(1024, 600)
        self.centralWidget = QtWidgets.QWidget(itemSuggestion)
        self.centralWidget.setObjectName("centralWidget")
        self.lblStatus = QtWidgets.QLabel(self.centralWidget)
        self.lblStatus.setGeometry(QtCore.QRect(30, 30, 961, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.btnChangePassword = QtWidgets.QPushButton(self.centralWidget)
        self.btnChangePassword.setGeometry(QtCore.QRect(30, 320, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnChangePassword.setFont(font)
        self.btnChangePassword.setObjectName("btnChangePassword")
        self.btnChangeUserDetail = QtWidgets.QPushButton(self.centralWidget)
        self.btnChangeUserDetail.setGeometry(QtCore.QRect(360, 320, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnChangeUserDetail.setFont(font)
        self.btnChangeUserDetail.setObjectName("btnChangeUserDetail")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 90, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 90, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.btnLogout = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogout.setGeometry(QtCore.QRect(690, 320, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLogout.setFont(font)
        self.btnLogout.setObjectName("btnLogout")
        self.lblItem1 = QtWidgets.QLabel(self.centralWidget)
        self.lblItem1.setGeometry(QtCore.QRect(30, 90, 311, 211))
        self.lblItem1.setText("")
        self.lblItem1.setObjectName("lblItem1")
        itemSuggestion.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(itemSuggestion)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName("menuBar")
        itemSuggestion.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(itemSuggestion)
        self.mainToolBar.setObjectName("mainToolBar")
        itemSuggestion.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(itemSuggestion)
        self.statusBar.setObjectName("statusBar")
        itemSuggestion.setStatusBar(self.statusBar)

        self.retranslateUi(itemSuggestion)
        QtCore.QMetaObject.connectSlotsByName(itemSuggestion)

    def retranslateUi(self, itemSuggestion):
        _translate = QtCore.QCoreApplication.translate
        itemSuggestion.setWindowTitle(_translate("itemSuggestion", "smartScaleGUI"))
        self.btnChangePassword.setText(_translate("itemSuggestion", "Change Password"))
        self.btnChangeUserDetail.setText(_translate("itemSuggestion", "Change User Detail"))
        self.pushButton_4.setText(_translate("itemSuggestion", "/"))
        self.pushButton_5.setText(_translate("itemSuggestion", "/"))
        self.btnLogout.setText(_translate("itemSuggestion", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemSuggestion = QtWidgets.QMainWindow()
    ui = Ui_itemSuggestion()
    ui.setupUi(itemSuggestion)
    itemSuggestion.show()
    sys.exit(app.exec_())

