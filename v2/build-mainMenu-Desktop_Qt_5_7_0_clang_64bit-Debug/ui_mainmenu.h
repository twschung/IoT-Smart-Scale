/********************************************************************************
** Form generated from reading UI file 'mainmenu.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINMENU_H
#define UI_MAINMENU_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_mainMenu
{
public:
    QGridLayout *gridLayout;
    QLabel *lbl_title;
    QPushButton *btn_login;
    QPushButton *btn_guest;
    QPushButton *btn_scaleOnly;
    QPushButton *btn_userSetup;

    void setupUi(QWidget *mainMenu)
    {
        if (mainMenu->objectName().isEmpty())
            mainMenu->setObjectName(QStringLiteral("mainMenu"));
        mainMenu->resize(800, 480);
        gridLayout = new QGridLayout(mainMenu);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        lbl_title = new QLabel(mainMenu);
        lbl_title->setObjectName(QStringLiteral("lbl_title"));
        lbl_title->setMinimumSize(QSize(341, 20));
        QFont font;
        font.setFamily(QStringLiteral("Helvetica Neue"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        lbl_title->setFont(font);

        gridLayout->addWidget(lbl_title, 0, 0, 1, 1);

        btn_login = new QPushButton(mainMenu);
        btn_login->setObjectName(QStringLiteral("btn_login"));
        btn_login->setMinimumSize(QSize(341, 191));
        QFont font1;
        font1.setFamily(QStringLiteral("Helvetica Neue"));
        font1.setPointSize(14);
        btn_login->setFont(font1);

        gridLayout->addWidget(btn_login, 1, 0, 1, 1);

        btn_guest = new QPushButton(mainMenu);
        btn_guest->setObjectName(QStringLiteral("btn_guest"));
        btn_guest->setMinimumSize(QSize(341, 191));
        btn_guest->setFont(font1);

        gridLayout->addWidget(btn_guest, 1, 1, 1, 1);

        btn_scaleOnly = new QPushButton(mainMenu);
        btn_scaleOnly->setObjectName(QStringLiteral("btn_scaleOnly"));
        btn_scaleOnly->setMinimumSize(QSize(341, 191));
        btn_scaleOnly->setFont(font1);

        gridLayout->addWidget(btn_scaleOnly, 2, 0, 1, 1);

        btn_userSetup = new QPushButton(mainMenu);
        btn_userSetup->setObjectName(QStringLiteral("btn_userSetup"));
        btn_userSetup->setMinimumSize(QSize(341, 191));
        btn_userSetup->setFont(font1);

        gridLayout->addWidget(btn_userSetup, 2, 1, 1, 1);


        retranslateUi(mainMenu);

        QMetaObject::connectSlotsByName(mainMenu);
    } // setupUi

    void retranslateUi(QWidget *mainMenu)
    {
        mainMenu->setWindowTitle(QApplication::translate("mainMenu", "mainMenu", 0));
        lbl_title->setText(QApplication::translate("mainMenu", "IoT Smart Scale", 0));
        btn_login->setText(QApplication::translate("mainMenu", "Login", 0));
        btn_guest->setText(QApplication::translate("mainMenu", "Guest", 0));
        btn_scaleOnly->setText(QApplication::translate("mainMenu", "Scale Only", 0));
        btn_userSetup->setText(QApplication::translate("mainMenu", "User Setup", 0));
    } // retranslateUi

};

namespace Ui {
    class mainMenu: public Ui_mainMenu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINMENU_H
