/********************************************************************************
** Form generated from reading UI file 'loginmenu.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGINMENU_H
#define UI_LOGINMENU_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_loginMenu
{
public:
    QGridLayout *gridLayout;
    QLabel *lbl_title;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QGridLayout *gridLayout_3;
    QPushButton *btn_user5;
    QPushButton *btn_user6;
    QPushButton *btn_user4;
    QPushButton *btn_user3;
    QPushButton *btn_user2;
    QPushButton *btn_user1;
    QPushButton *btn_newLogin;
    QSpacerItem *horizontalSpacer;
    QPushButton *btn_back;

    void setupUi(QWidget *loginMenu)
    {
        if (loginMenu->objectName().isEmpty())
            loginMenu->setObjectName(QStringLiteral("loginMenu"));
        loginMenu->resize(800, 480);
        gridLayout = new QGridLayout(loginMenu);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        lbl_title = new QLabel(loginMenu);
        lbl_title->setObjectName(QStringLiteral("lbl_title"));
        lbl_title->setMinimumSize(QSize(381, 70));
        QFont font;
        font.setFamily(QStringLiteral("Helvetica Neue"));
        font.setPointSize(24);
        font.setBold(true);
        font.setWeight(75);
        lbl_title->setFont(font);

        gridLayout->addWidget(lbl_title, 0, 0, 1, 2);

        scrollArea = new QScrollArea(loginMenu);
        scrollArea->setObjectName(QStringLiteral("scrollArea"));
        scrollArea->setMinimumSize(QSize(781, 321));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QStringLiteral("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 779, 319));
        scrollAreaWidgetContents->setMinimumSize(QSize(779, 319));
        gridLayout_3 = new QGridLayout(scrollAreaWidgetContents);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        btn_user5 = new QPushButton(scrollAreaWidgetContents);
        btn_user5->setObjectName(QStringLiteral("btn_user5"));
        btn_user5->setMinimumSize(QSize(250, 161));
        QFont font1;
        font1.setFamily(QStringLiteral("Helvetica Neue"));
        font1.setPointSize(16);
        btn_user5->setFont(font1);

        gridLayout_3->addWidget(btn_user5, 1, 1, 1, 1);

        btn_user6 = new QPushButton(scrollAreaWidgetContents);
        btn_user6->setObjectName(QStringLiteral("btn_user6"));
        btn_user6->setMinimumSize(QSize(250, 161));
        btn_user6->setFont(font1);

        gridLayout_3->addWidget(btn_user6, 1, 2, 1, 1);

        btn_user4 = new QPushButton(scrollAreaWidgetContents);
        btn_user4->setObjectName(QStringLiteral("btn_user4"));
        btn_user4->setMinimumSize(QSize(250, 161));
        btn_user4->setFont(font1);

        gridLayout_3->addWidget(btn_user4, 1, 0, 1, 1);

        btn_user3 = new QPushButton(scrollAreaWidgetContents);
        btn_user3->setObjectName(QStringLiteral("btn_user3"));
        btn_user3->setMinimumSize(QSize(250, 161));
        btn_user3->setFont(font1);

        gridLayout_3->addWidget(btn_user3, 0, 2, 1, 1);

        btn_user2 = new QPushButton(scrollAreaWidgetContents);
        btn_user2->setObjectName(QStringLiteral("btn_user2"));
        btn_user2->setMinimumSize(QSize(250, 161));
        btn_user2->setFont(font1);

        gridLayout_3->addWidget(btn_user2, 0, 1, 1, 1);

        btn_user1 = new QPushButton(scrollAreaWidgetContents);
        btn_user1->setObjectName(QStringLiteral("btn_user1"));
        btn_user1->setMinimumSize(QSize(250, 161));
        btn_user1->setFont(font1);

        gridLayout_3->addWidget(btn_user1, 0, 0, 1, 1);

        scrollArea->setWidget(scrollAreaWidgetContents);

        gridLayout->addWidget(scrollArea, 1, 0, 1, 3);

        btn_newLogin = new QPushButton(loginMenu);
        btn_newLogin->setObjectName(QStringLiteral("btn_newLogin"));
        btn_newLogin->setMinimumSize(QSize(250, 61));
        btn_newLogin->setFont(font1);

        gridLayout->addWidget(btn_newLogin, 2, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(269, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 2, 1, 1, 1);

        btn_back = new QPushButton(loginMenu);
        btn_back->setObjectName(QStringLiteral("btn_back"));
        btn_back->setMinimumSize(QSize(250, 61));
        btn_back->setFont(font1);

        gridLayout->addWidget(btn_back, 2, 2, 1, 1);


        retranslateUi(loginMenu);

        QMetaObject::connectSlotsByName(loginMenu);
    } // setupUi

    void retranslateUi(QWidget *loginMenu)
    {
        loginMenu->setWindowTitle(QApplication::translate("loginMenu", "Form", 0));
        lbl_title->setText(QApplication::translate("loginMenu", "Who are you?", 0));
        btn_user5->setText(QApplication::translate("loginMenu", "User 5", 0));
        btn_user6->setText(QApplication::translate("loginMenu", "User 6", 0));
        btn_user4->setText(QApplication::translate("loginMenu", "User 4", 0));
        btn_user3->setText(QApplication::translate("loginMenu", "User 3", 0));
        btn_user2->setText(QApplication::translate("loginMenu", "User 2", 0));
        btn_user1->setText(QApplication::translate("loginMenu", "User 1", 0));
        btn_newLogin->setText(QApplication::translate("loginMenu", "New Login", 0));
        btn_back->setText(QApplication::translate("loginMenu", "Back", 0));
    } // retranslateUi

};

namespace Ui {
    class loginMenu: public Ui_loginMenu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGINMENU_H
