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
        itemSuggestion.resize(1024, 565)
        self.centralWidget = QtWidgets.QWidget(itemSuggestion)
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
        self.btnLogout = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogout.setGeometry(QtCore.QRect(680, 300, 311, 211))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLogout.setFont(font)
        self.btnLogout.setObjectName("btnLogout")
        self.lblItem1 = QtWidgets.QLabel(self.centralWidget)
        self.lblItem1.setGeometry(QtCore.QRect(20, 70, 311, 211))
        self.lblItem1.setFrameShape(QtWidgets.QFrame.Box)
        self.lblItem1.setText("")
        self.lblItem1.setObjectName("lblItem1")
        self.lblItem2 = QtWidgets.QLabel(self.centralWidget)
        self.lblItem2.setGeometry(QtCore.QRect(350, 70, 311, 211))
        self.lblItem2.setFrameShape(QtWidgets.QFrame.Box)
        self.lblItem2.setText("")
        self.lblItem2.setObjectName("lblItem2")
        self.lblItem3 = QtWidgets.QLabel(self.centralWidget)
        self.lblItem3.setGeometry(QtCore.QRect(680, 70, 311, 211))
        self.lblItem3.setFrameShape(QtWidgets.QFrame.Box)
        self.lblItem3.setText("")
        self.lblItem3.setObjectName("lblItem3")
        self.lblItem4 = QtWidgets.QLabel(self.centralWidget)
        self.lblItem4.setGeometry(QtCore.QRect(20, 300, 311, 211))
        self.lblItem4.setFrameShape(QtWidgets.QFrame.Box)
        self.lblItem4.setText("")
        self.lblItem4.setObjectName("lblItem4")
        self.lblItem5 = QtWidgets.QLabel(self.centralWidget)
        self.lblItem5.setGeometry(QtCore.QRect(350, 300, 311, 211))
        self.lblItem5.setFrameShape(QtWidgets.QFrame.Box)
        self.lblItem5.setText("")
        self.lblItem5.setObjectName("lblItem5")
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
        self.btnLogout.setText(_translate("itemSuggestion", "Fetch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemSuggestion = QtWidgets.QMainWindow()
    ui = Ui_itemSuggestion()
    ui.setupUi(itemSuggestion)
    itemSuggestion.show()
    sys.exit(app.exec_())

