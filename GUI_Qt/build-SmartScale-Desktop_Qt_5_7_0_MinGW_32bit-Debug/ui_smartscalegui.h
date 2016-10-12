/********************************************************************************
** Form generated from reading UI file 'smartscalegui.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SMARTSCALEGUI_H
#define UI_SMARTSCALEGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_smartScaleGUI
{
public:
    QWidget *centralWidget;
    QTextEdit *txtUserName;
    QTextEdit *txtPassword;
    QPushButton *btnLogin;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *smartScaleGUI)
    {
        if (smartScaleGUI->objectName().isEmpty())
            smartScaleGUI->setObjectName(QStringLiteral("smartScaleGUI"));
        smartScaleGUI->resize(1024, 600);
        centralWidget = new QWidget(smartScaleGUI);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        txtUserName = new QTextEdit(centralWidget);
        txtUserName->setObjectName(QStringLiteral("txtUserName"));
        txtUserName->setGeometry(QRect(200, 170, 231, 31));
        txtPassword = new QTextEdit(centralWidget);
        txtPassword->setObjectName(QStringLiteral("txtPassword"));
        txtPassword->setGeometry(QRect(200, 210, 231, 31));
        btnLogin = new QPushButton(centralWidget);
        btnLogin->setObjectName(QStringLiteral("btnLogin"));
        btnLogin->setGeometry(QRect(450, 170, 161, 31));
        smartScaleGUI->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(smartScaleGUI);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1024, 21));
        smartScaleGUI->setMenuBar(menuBar);
        mainToolBar = new QToolBar(smartScaleGUI);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        smartScaleGUI->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(smartScaleGUI);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        smartScaleGUI->setStatusBar(statusBar);

        retranslateUi(smartScaleGUI);

        QMetaObject::connectSlotsByName(smartScaleGUI);
    } // setupUi

    void retranslateUi(QMainWindow *smartScaleGUI)
    {
        smartScaleGUI->setWindowTitle(QApplication::translate("smartScaleGUI", "smartScaleGUI", 0));
        btnLogin->setText(QApplication::translate("smartScaleGUI", "Login", 0));
    } // retranslateUi

};

namespace Ui {
    class smartScaleGUI: public Ui_smartScaleGUI {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SMARTSCALEGUI_H
