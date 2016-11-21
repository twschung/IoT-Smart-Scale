# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userDetails.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userDetails(object):
    def setupUi(self, userDetails):
        userDetails.setObjectName("userDetails")
        userDetails.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(userDetails)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.grdGraphs = QtWidgets.QGridLayout()
        self.grdGraphs.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grdGraphs.setContentsMargins(11, 11, 11, 11)
        self.grdGraphs.setSpacing(6)
        self.grdGraphs.setObjectName("grdGraphs")
        self.grphVisuals2 = QtWidgets.QGraphicsView(self.centralWidget)
        self.grphVisuals2.setMinimumSize(QtCore.QSize(303, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grphVisuals2.setFont(font)
        self.grphVisuals2.setObjectName("grphVisuals2")
        self.grdGraphs.addWidget(self.grphVisuals2, 3, 0, 1, 1)
        self.lblCurrenvsLast = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblCurrenvsLast.setFont(font)
        self.lblCurrenvsLast.setObjectName("lblCurrenvsLast")
        self.grdGraphs.addWidget(self.lblCurrenvsLast, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lblVisuals2Title = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblVisuals2Title.setFont(font)
        self.lblVisuals2Title.setObjectName("lblVisuals2Title")
        self.grdGraphs.addWidget(self.lblVisuals2Title, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.grphCurretvsLast = QtWidgets.QGraphicsView(self.centralWidget)
        self.grphCurretvsLast.setMinimumSize(QtCore.QSize(303, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grphCurretvsLast.setFont(font)
        self.grphCurretvsLast.setObjectName("grphCurretvsLast")
        self.grdGraphs.addWidget(self.grphCurretvsLast, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.grdGraphs, 1, 1, 4, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lblName = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblName.setFont(font)
        self.lblName.setObjectName("lblName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblUserName = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblUserName.setFont(font)
        self.lblUserName.setObjectName("lblUserName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblUserName)
        self.lblEmail = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblEmail)
        self.lblUserEmail = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblUserEmail.setFont(font)
        self.lblUserEmail.setObjectName("lblUserEmail")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblUserEmail)
        self.lblAge = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblAge.setFont(font)
        self.lblAge.setObjectName("lblAge")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblAge)
        self.lblUserAge = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblUserAge.setFont(font)
        self.lblUserAge.setObjectName("lblUserAge")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblUserAge)
        self.lblHeight = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblHeight.setFont(font)
        self.lblHeight.setObjectName("lblHeight")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblHeight)
        self.lblUserHeight = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblUserHeight.setFont(font)
        self.lblUserHeight.setObjectName("lblUserHeight")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lblUserHeight)
        self.lblWeight = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblWeight.setFont(font)
        self.lblWeight.setObjectName("lblWeight")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblWeight)
        self.lblUserWeight = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblUserWeight.setFont(font)
        self.lblUserWeight.setObjectName("lblUserWeight")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lblUserWeight)
        self.lblBMI = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblBMI.setFont(font)
        self.lblBMI.setObjectName("lblBMI")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblBMI)
        self.lblUserBMI = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblUserBMI.setFont(font)
        self.lblUserBMI.setObjectName("lblUserBMI")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lblUserBMI)
        self.lblBMR = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblBMR.setFont(font)
        self.lblBMR.setObjectName("lblBMR")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblBMR)
        self.lblUserBMR = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblUserBMR.setFont(font)
        self.lblUserBMR.setObjectName("lblUserBMR")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lblUserBMR)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.btnBack = QtWidgets.QPushButton(self.centralWidget)
        self.btnBack.setMaximumSize(QtCore.QSize(131, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 5, 0, 1, 1)
        self.lblUserDetails = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.lblUserDetails.setFont(font)
        self.lblUserDetails.setObjectName("lblUserDetails")
        self.gridLayout.addWidget(self.lblUserDetails, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setMinimumSize(QtCore.QSize(455, 135))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frmDailyCals = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frmDailyCals.setFont(font)
        self.frmDailyCals.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDailyCals.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDailyCals.setObjectName("frmDailyCals")
        self.pgrsDailyIntake = QtWidgets.QProgressBar(self.frmDailyCals)
        self.pgrsDailyIntake.setGeometry(QtCore.QRect(30, 30, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pgrsDailyIntake.setFont(font)
        self.pgrsDailyIntake.setProperty("value", 24)
        self.pgrsDailyIntake.setObjectName("pgrsDailyIntake")
        self.lblDailyCals = QtWidgets.QLabel(self.frmDailyCals)
        self.lblDailyCals.setGeometry(QtCore.QRect(30, 80, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblDailyCals.setFont(font)
        self.lblDailyCals.setObjectName("lblDailyCals")
        self.gridLayout_2.addWidget(self.frmDailyCals, 0, 0, 1, 1)
        self.frmFitnessMeasure2 = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frmFitnessMeasure2.setFont(font)
        self.frmFitnessMeasure2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmFitnessMeasure2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmFitnessMeasure2.setObjectName("frmFitnessMeasure2")
        self.prgsFitnessMeausre2 = QtWidgets.QProgressBar(self.frmFitnessMeasure2)
        self.prgsFitnessMeausre2.setGeometry(QtCore.QRect(27, 30, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.prgsFitnessMeausre2.setFont(font)
        self.prgsFitnessMeausre2.setProperty("value", 24)
        self.prgsFitnessMeausre2.setObjectName("prgsFitnessMeausre2")
        self.lblFitnessMeasure2 = QtWidgets.QLabel(self.frmFitnessMeasure2)
        self.lblFitnessMeasure2.setGeometry(QtCore.QRect(30, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.lblFitnessMeasure2.setFont(font)
        self.lblFitnessMeasure2.setObjectName("lblFitnessMeasure2")
        self.gridLayout_2.addWidget(self.frmFitnessMeasure2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        userDetails.setCentralWidget(self.centralWidget)

        self.retranslateUi(userDetails)
        QtCore.QMetaObject.connectSlotsByName(userDetails)

    def retranslateUi(self, userDetails):
        _translate = QtCore.QCoreApplication.translate
        userDetails.setWindowTitle(_translate("userDetails", "smartScaleGUI"))
        self.lblCurrenvsLast.setText(_translate("userDetails", "This week\'s vs Last Week\'s Intake"))
        self.lblVisuals2Title.setText(_translate("userDetails", "Some other graphical data representation"))
        self.lblName.setText(_translate("userDetails", "Name:"))
        self.lblUserName.setText(_translate("userDetails", "usersname"))
        self.lblEmail.setText(_translate("userDetails", "Email: "))
        self.lblUserEmail.setText(_translate("userDetails", "useremail"))
        self.lblAge.setText(_translate("userDetails", "Age:"))
        self.lblUserAge.setText(_translate("userDetails", "usersage"))
        self.lblHeight.setText(_translate("userDetails", "Height:"))
        self.lblUserHeight.setText(_translate("userDetails", "usersheight"))
        self.lblWeight.setText(_translate("userDetails", "Weight:"))
        self.lblUserWeight.setText(_translate("userDetails", "usersweight"))
        self.lblBMI.setText(_translate("userDetails", "BMI:"))
        self.lblUserBMI.setText(_translate("userDetails", "usersbmi"))
        self.lblBMR.setText(_translate("userDetails", "BMR:"))
        self.lblUserBMR.setText(_translate("userDetails", "usersbmr"))
        self.btnBack.setText(_translate("userDetails", "Back"))
        self.lblUserDetails.setText(_translate("userDetails", "User Details"))
        self.lblDailyCals.setText(_translate("userDetails", "xxxx/xxxx kcals"))
        self.lblFitnessMeasure2.setText(_translate("userDetails", "Some other measure"))

