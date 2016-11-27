/********************************************************************************
** Form generated from reading UI file 'foodsuggestionmenu.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FOODSUGGESTIONMENU_H
#define UI_FOODSUGGESTIONMENU_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_foodSuggestionMenu
{
public:
    QGridLayout *gridLayout;
    QLabel *lbl_title;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QGridLayout *gridLayout_3;
    QPushButton *btn_item5;
    QPushButton *btn_item6;
    QPushButton *btn_item4;
    QPushButton *btn_item3;
    QPushButton *btn_item2;
    QPushButton *btn_item1;
    QPushButton *btn_notFound;
    QPushButton *btn_back;

    void setupUi(QWidget *foodSuggestionMenu)
    {
        if (foodSuggestionMenu->objectName().isEmpty())
            foodSuggestionMenu->setObjectName(QStringLiteral("foodSuggestionMenu"));
        foodSuggestionMenu->resize(800, 480);
        gridLayout = new QGridLayout(foodSuggestionMenu);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        lbl_title = new QLabel(foodSuggestionMenu);
        lbl_title->setObjectName(QStringLiteral("lbl_title"));
        lbl_title->setMinimumSize(QSize(381, 70));
        QFont font;
        font.setFamily(QStringLiteral("Helvetica Neue"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        lbl_title->setFont(font);

        gridLayout->addWidget(lbl_title, 0, 0, 1, 1);

        scrollArea = new QScrollArea(foodSuggestionMenu);
        scrollArea->setObjectName(QStringLiteral("scrollArea"));
        scrollArea->setMinimumSize(QSize(781, 321));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QStringLiteral("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 779, 319));
        scrollAreaWidgetContents->setMinimumSize(QSize(779, 319));
        gridLayout_3 = new QGridLayout(scrollAreaWidgetContents);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        btn_item5 = new QPushButton(scrollAreaWidgetContents);
        btn_item5->setObjectName(QStringLiteral("btn_item5"));
        btn_item5->setMinimumSize(QSize(250, 161));

        gridLayout_3->addWidget(btn_item5, 1, 1, 1, 1);

        btn_item6 = new QPushButton(scrollAreaWidgetContents);
        btn_item6->setObjectName(QStringLiteral("btn_item6"));
        btn_item6->setMinimumSize(QSize(250, 161));

        gridLayout_3->addWidget(btn_item6, 1, 2, 1, 1);

        btn_item4 = new QPushButton(scrollAreaWidgetContents);
        btn_item4->setObjectName(QStringLiteral("btn_item4"));
        btn_item4->setMinimumSize(QSize(250, 161));

        gridLayout_3->addWidget(btn_item4, 1, 0, 1, 1);

        btn_item3 = new QPushButton(scrollAreaWidgetContents);
        btn_item3->setObjectName(QStringLiteral("btn_item3"));
        btn_item3->setMinimumSize(QSize(250, 161));

        gridLayout_3->addWidget(btn_item3, 0, 2, 1, 1);

        btn_item2 = new QPushButton(scrollAreaWidgetContents);
        btn_item2->setObjectName(QStringLiteral("btn_item2"));
        btn_item2->setMinimumSize(QSize(250, 161));

        gridLayout_3->addWidget(btn_item2, 0, 1, 1, 1);

        btn_item1 = new QPushButton(scrollAreaWidgetContents);
        btn_item1->setObjectName(QStringLiteral("btn_item1"));
        btn_item1->setMinimumSize(QSize(250, 161));

        gridLayout_3->addWidget(btn_item1, 0, 0, 1, 1);

        scrollArea->setWidget(scrollAreaWidgetContents);

        gridLayout->addWidget(scrollArea, 1, 0, 1, 2);

        btn_notFound = new QPushButton(foodSuggestionMenu);
        btn_notFound->setObjectName(QStringLiteral("btn_notFound"));
        btn_notFound->setMinimumSize(QSize(250, 61));

        gridLayout->addWidget(btn_notFound, 2, 0, 1, 1);

        btn_back = new QPushButton(foodSuggestionMenu);
        btn_back->setObjectName(QStringLiteral("btn_back"));
        btn_back->setMinimumSize(QSize(250, 61));

        gridLayout->addWidget(btn_back, 2, 1, 1, 1);


        retranslateUi(foodSuggestionMenu);

        QMetaObject::connectSlotsByName(foodSuggestionMenu);
    } // setupUi

    void retranslateUi(QWidget *foodSuggestionMenu)
    {
        foodSuggestionMenu->setWindowTitle(QApplication::translate("foodSuggestionMenu", "foodSuggestionMenu", 0));
        lbl_title->setText(QApplication::translate("foodSuggestionMenu", "Our suggested food items:", 0));
        btn_item5->setText(QApplication::translate("foodSuggestionMenu", "Item 5", 0));
        btn_item6->setText(QApplication::translate("foodSuggestionMenu", "Item 6", 0));
        btn_item4->setText(QApplication::translate("foodSuggestionMenu", "Item 4", 0));
        btn_item3->setText(QApplication::translate("foodSuggestionMenu", "Item 3", 0));
        btn_item2->setText(QApplication::translate("foodSuggestionMenu", "Item 2", 0));
        btn_item1->setText(QApplication::translate("foodSuggestionMenu", "Item 1", 0));
        btn_notFound->setText(QApplication::translate("foodSuggestionMenu", "Not found?", 0));
        btn_back->setText(QApplication::translate("foodSuggestionMenu", "Back", 0));
    } // retranslateUi

};

namespace Ui {
    class foodSuggestionMenu: public Ui_foodSuggestionMenu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FOODSUGGESTIONMENU_H
