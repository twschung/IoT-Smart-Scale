# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getWeight.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_getWeight(object):
    def setupUi(self, getWeight):
        getWeight.setObjectName("getWeight")
        getWeight.resize(1024, 565)
        self.centralWidget = QtWidgets.QWidget(getWeight)
        self.centralWidget.setObjectName("centralWidget")
        self.btnBack = QtWidgets.QPushButton(self.centralWidget)
        self.btnBack.setGeometry(QtCore.QRect(60, 450, 201, 31))
        self.btnBack.setObjectName("btnBack")
        self.btnTare = QtWidgets.QPushButton(self.centralWidget)
        self.btnTare.setGeometry(QtCore.QRect(270, 450, 201, 31))
        self.btnTare.setObjectName("btnTare")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(90, 320, 331, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblGrams = QtWidgets.QLabel(self.frame)
        self.lblGrams.setGeometry(QtCore.QRect(260, 50, 41, 61))
        self.lblGrams.setObjectName("lblGrams")
        self.lcdWeight = QtWidgets.QLCDNumber(self.frame)
        self.lcdWeight.setGeometry(QtCore.QRect(30, 20, 221, 91))
        self.lcdWeight.setObjectName("lcdWeight")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(605, 100, 301, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblFoodCat = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblFoodCat.setMaximumSize(QtCore.QSize(94, 16))
        self.lblFoodCat.setObjectName("lblFoodCat")
        self.gridLayout_2.addWidget(self.lblFoodCat, 0, 0, 1, 1)
        self.lblCategory = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblCategory.setObjectName("lblCategory")
        self.gridLayout_2.addWidget(self.lblCategory, 0, 1, 1, 1)
        self.lblObj = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblObj.setMaximumSize(QtCore.QSize(94, 16))
        self.lblObj.setObjectName("lblObj")
        self.gridLayout_2.addWidget(self.lblObj, 1, 0, 1, 1)
        self.lblObject = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblObject.setObjectName("lblObject")
        self.gridLayout_2.addWidget(self.lblObject, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 421, 16))
        self.label.setObjectName("label")
        self.btnBack_2 = QtWidgets.QPushButton(self.centralWidget)
        self.btnBack_2.setGeometry(QtCore.QRect(615, 450, 201, 31))
        self.btnBack_2.setObjectName("btnBack_2")
        self.imgFoodItem = QtWidgets.QGraphicsView(self.centralWidget)
        self.imgFoodItem.setGeometry(QtCore.QRect(120, 80, 261, 201))
        self.imgFoodItem.setObjectName("imgFoodItem")
        self.lblNutritionalnformation = QtWidgets.QLabel(self.centralWidget)
        self.lblNutritionalnformation.setGeometry(QtCore.QRect(605, 210, 201, 31))
        self.lblNutritionalnformation.setAcceptDrops(False)
        self.lblNutritionalnformation.setAutoFillBackground(False)
        self.lblNutritionalnformation.setObjectName("lblNutritionalnformation")
        self.lblFatVal = QtWidgets.QLabel(self.centralWidget)
        self.lblFatVal.setGeometry(QtCore.QRect(730, 376, 52, 16))
        self.lblFatVal.setObjectName("lblFatVal")
        self.lblSugar = QtWidgets.QLabel(self.centralWidget)
        self.lblSugar.setGeometry(QtCore.QRect(666, 310, 56, 16))
        self.lblSugar.setMaximumSize(QtCore.QSize(56, 16))
        self.lblSugar.setObjectName("lblSugar")
        self.lblProteinVal = QtWidgets.QLabel(self.centralWidget)
        self.lblProteinVal.setGeometry(QtCore.QRect(730, 276, 75, 16))
        self.lblProteinVal.setObjectName("lblProteinVal")
        self.lblFbreVal = QtWidgets.QLabel(self.centralWidget)
        self.lblFbreVal.setGeometry(QtCore.QRect(730, 342, 63, 16))
        self.lblFbreVal.setObjectName("lblFbreVal")
        self.lblFibre = QtWidgets.QLabel(self.centralWidget)
        self.lblFibre.setGeometry(QtCore.QRect(671, 342, 51, 16))
        self.lblFibre.setMaximumSize(QtCore.QSize(51, 16))
        self.lblFibre.setObjectName("lblFibre")
        self.lblFat = QtWidgets.QLabel(self.centralWidget)
        self.lblFat.setGeometry(QtCore.QRect(682, 376, 40, 16))
        self.lblFat.setMaximumSize(QtCore.QSize(40, 16))
        self.lblFat.setObjectName("lblFat")
        self.lblSaltVal = QtWidgets.QLabel(self.centralWidget)
        self.lblSaltVal.setGeometry(QtCore.QRect(730, 410, 53, 16))
        self.lblSaltVal.setObjectName("lblSaltVal")
        self.lblSalt = QtWidgets.QLabel(self.centralWidget)
        self.lblSalt.setGeometry(QtCore.QRect(678, 410, 44, 16))
        self.lblSalt.setMaximumSize(QtCore.QSize(44, 16))
        self.lblSalt.setObjectName("lblSalt")
        self.lblEnergyVal = QtWidgets.QLabel(self.centralWidget)
        self.lblEnergyVal.setGeometry(QtCore.QRect(730, 242, 75, 16))
        self.lblEnergyVal.setObjectName("lblEnergyVal")
        self.lblProtein = QtWidgets.QLabel(self.centralWidget)
        self.lblProtein.setGeometry(QtCore.QRect(658, 276, 64, 16))
        self.lblProtein.setMaximumSize(QtCore.QSize(64, 16))
        self.lblProtein.setObjectName("lblProtein")
        self.lblEnergy = QtWidgets.QLabel(self.centralWidget)
        self.lblEnergy.setGeometry(QtCore.QRect(607, 242, 115, 16))
        self.lblEnergy.setMaximumSize(QtCore.QSize(115, 16))
        self.lblEnergy.setObjectName("lblEnergy")
        self.lblSugarVal = QtWidgets.QLabel(self.centralWidget)
        self.lblSugarVal.setGeometry(QtCore.QRect(730, 310, 69, 16))
        self.lblSugarVal.setObjectName("lblSugarVal")
        getWeight.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(getWeight)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menuBar.setObjectName("menuBar")
        getWeight.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(getWeight)
        self.mainToolBar.setObjectName("mainToolBar")
        getWeight.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(getWeight)
        self.statusBar.setObjectName("statusBar")
        getWeight.setStatusBar(self.statusBar)

        self.retranslateUi(getWeight)
        QtCore.QMetaObject.connectSlotsByName(getWeight)

    def retranslateUi(self, getWeight):
        _translate = QtCore.QCoreApplication.translate
        getWeight.setWindowTitle(_translate("getWeight", "smartScaleGUI"))
        self.btnBack.setText(_translate("getWeight", "Back"))
        self.btnTare.setText(_translate("getWeight", "Tare"))
        self.lblGrams.setText(_translate("getWeight", "<html><head/><body><p><span style=\" font-size:48pt;\">g</span></p></body></html>"))
        self.lblFoodCat.setText(_translate("getWeight", "Food Category:"))
        self.lblCategory.setText(_translate("getWeight", "lblCategory"))
        self.lblObj.setText(_translate("getWeight", "Food Object:"))
        self.lblObject.setText(_translate("getWeight", "lblObject"))
        self.label.setText(_translate("getWeight", "Place food item on the scale"))
        self.btnBack_2.setText(_translate("getWeight", "Add to daily intake"))
        self.lblNutritionalnformation.setText(_translate("getWeight", "<html><head/><body><p><span style=\" font-weight:600;\">Nutritional Information</span></p></body></html>"))
        self.lblFatVal.setText(_translate("getWeight", "lblFatVal"))
        self.lblSugar.setText(_translate("getWeight", "Sugar (g)"))
        self.lblProteinVal.setText(_translate("getWeight", "lblProteinVal"))
        self.lblFbreVal.setText(_translate("getWeight", "lblFibreVal"))
        self.lblFibre.setText(_translate("getWeight", "Fibre (g)"))
        self.lblFat.setText(_translate("getWeight", "Fat (g)"))
        self.lblSaltVal.setText(_translate("getWeight", "lbSaltVal"))
        self.lblSalt.setText(_translate("getWeight", "Salt (g)"))
        self.lblEnergyVal.setText(_translate("getWeight", "lblEnergyVal"))
        self.lblProtein.setText(_translate("getWeight", "Protein (g)"))
        self.lblEnergy.setText(_translate("getWeight", "Energy value (kcal)"))
        self.lblSugarVal.setText(_translate("getWeight", "lblSugarVal"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    getWeight = QtWidgets.QMainWindow()
    ui = Ui_getWeight()
    ui.setupUi(getWeight)
    getWeight.show()
    sys.exit(app.exec_())