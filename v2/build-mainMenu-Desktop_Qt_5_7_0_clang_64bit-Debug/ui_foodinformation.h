/********************************************************************************
** Form generated from reading UI file 'foodinformation.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FOODINFORMATION_H
#define UI_FOODINFORMATION_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_foodInformation
{
public:
    QGridLayout *gridLayout;
    QLabel *lbl_foodInfo;
    QGraphicsView *pic_foodItem;
    QGroupBox *grpBx_nutriInfo;
    QFrame *frame_lcd;
    QGridLayout *gridLayout_2;
    QLCDNumber *lcd_number;
    QLabel *lbl_g;
    QPushButton *btn_tare;
    QPushButton *btn_addIntake;
    QPushButton *btn_new;
    QPushButton *btn_back;

    void setupUi(QWidget *foodInformation)
    {
        if (foodInformation->objectName().isEmpty())
            foodInformation->setObjectName(QStringLiteral("foodInformation"));
        foodInformation->resize(800, 480);
        gridLayout = new QGridLayout(foodInformation);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        lbl_foodInfo = new QLabel(foodInformation);
        lbl_foodInfo->setObjectName(QStringLiteral("lbl_foodInfo"));
        lbl_foodInfo->setMinimumSize(QSize(231, 20));
        QFont font;
        font.setFamily(QStringLiteral("Helvetica Neue"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        lbl_foodInfo->setFont(font);

        gridLayout->addWidget(lbl_foodInfo, 0, 0, 1, 1);

        pic_foodItem = new QGraphicsView(foodInformation);
        pic_foodItem->setObjectName(QStringLiteral("pic_foodItem"));
        pic_foodItem->setMinimumSize(QSize(441, 271));
        pic_foodItem->setFrameShadow(QFrame::Raised);

        gridLayout->addWidget(pic_foodItem, 1, 0, 1, 2);

        grpBx_nutriInfo = new QGroupBox(foodInformation);
        grpBx_nutriInfo->setObjectName(QStringLiteral("grpBx_nutriInfo"));
        grpBx_nutriInfo->setMinimumSize(QSize(201, 298));

        gridLayout->addWidget(grpBx_nutriInfo, 1, 2, 1, 1);

        frame_lcd = new QFrame(foodInformation);
        frame_lcd->setObjectName(QStringLiteral("frame_lcd"));
        frame_lcd->setMinimumSize(QSize(321, 101));
        frame_lcd->setFrameShape(QFrame::StyledPanel);
        frame_lcd->setFrameShadow(QFrame::Raised);
        gridLayout_2 = new QGridLayout(frame_lcd);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        lcd_number = new QLCDNumber(frame_lcd);
        lcd_number->setObjectName(QStringLiteral("lcd_number"));
        lcd_number->setMinimumSize(QSize(311, 81));

        gridLayout_2->addWidget(lcd_number, 0, 0, 1, 1);

        lbl_g = new QLabel(frame_lcd);
        lbl_g->setObjectName(QStringLiteral("lbl_g"));
        lbl_g->setMinimumSize(QSize(21, 41));
        QFont font1;
        font1.setFamily(QStringLiteral("Helvetica Neue"));
        font1.setPointSize(28);
        font1.setBold(true);
        font1.setWeight(75);
        lbl_g->setFont(font1);

        gridLayout_2->addWidget(lbl_g, 0, 1, 1, 1);


        gridLayout->addWidget(frame_lcd, 2, 0, 2, 1);

        btn_tare = new QPushButton(foodInformation);
        btn_tare->setObjectName(QStringLiteral("btn_tare"));
        btn_tare->setMinimumSize(QSize(101, 51));
        QFont font2;
        font2.setFamily(QStringLiteral("Helvetica Neue"));
        font2.setPointSize(14);
        btn_tare->setFont(font2);

        gridLayout->addWidget(btn_tare, 2, 1, 1, 1);

        btn_addIntake = new QPushButton(foodInformation);
        btn_addIntake->setObjectName(QStringLiteral("btn_addIntake"));
        btn_addIntake->setMinimumSize(QSize(161, 51));
        btn_addIntake->setFont(font2);

        gridLayout->addWidget(btn_addIntake, 2, 2, 1, 1);

        btn_new = new QPushButton(foodInformation);
        btn_new->setObjectName(QStringLiteral("btn_new"));
        btn_new->setMinimumSize(QSize(101, 51));
        btn_new->setFont(font2);

        gridLayout->addWidget(btn_new, 3, 1, 1, 1);

        btn_back = new QPushButton(foodInformation);
        btn_back->setObjectName(QStringLiteral("btn_back"));
        btn_back->setMinimumSize(QSize(161, 51));
        QPalette palette;
        QBrush brush(QColor(249, 249, 249, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Light, brush);
        QBrush brush1(QColor(255, 255, 255, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Base, brush1);
        QBrush brush2(QColor(214, 214, 214, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Window, brush2);
        palette.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Base, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush2);
        btn_back->setPalette(palette);
        btn_back->setFont(font2);

        gridLayout->addWidget(btn_back, 3, 2, 1, 1);


        retranslateUi(foodInformation);

        QMetaObject::connectSlotsByName(foodInformation);
    } // setupUi

    void retranslateUi(QWidget *foodInformation)
    {
        foodInformation->setWindowTitle(QApplication::translate("foodInformation", "Form", 0));
        lbl_foodInfo->setText(QApplication::translate("foodInformation", "Food Item Information", 0));
        grpBx_nutriInfo->setTitle(QString());
        lbl_g->setText(QApplication::translate("foodInformation", "g", 0));
        btn_tare->setText(QApplication::translate("foodInformation", "Tare", 0));
        btn_addIntake->setText(QApplication::translate("foodInformation", "Add to daily intake", 0));
        btn_new->setText(QApplication::translate("foodInformation", "New", 0));
        btn_back->setText(QApplication::translate("foodInformation", "Back", 0));
    } // retranslateUi

};

namespace Ui {
    class foodInformation: public Ui_foodInformation {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FOODINFORMATION_H
