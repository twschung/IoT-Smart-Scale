/********************************************************************************
** Form generated from reading UI file 'tared.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TARED_H
#define UI_TARED_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_tared
{
public:
    QLabel *label;
    QPushButton *btn_back;
    QLabel *label_2;

    void setupUi(QDialog *tared)
    {
        if (tared->objectName().isEmpty())
            tared->setObjectName(QStringLiteral("tared"));
        tared->resize(450, 300);
        label = new QLabel(tared);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(110, 130, 231, 21));
        QFont font;
        font.setFamily(QStringLiteral("Helvetica Neue"));
        font.setPointSize(14);
        label->setFont(font);
        btn_back = new QPushButton(tared);
        btn_back->setObjectName(QStringLiteral("btn_back"));
        btn_back->setGeometry(QRect(150, 220, 141, 51));
        btn_back->setFont(font);
        label_2 = new QLabel(tared);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(200, 100, 51, 41));
        label_2->setFont(font);

        retranslateUi(tared);

        QMetaObject::connectSlotsByName(tared);
    } // setupUi

    void retranslateUi(QDialog *tared)
    {
        tared->setWindowTitle(QApplication::translate("tared", "tared", 0));
        label->setText(QApplication::translate("tared", "You may now place your food item.", 0));
        btn_back->setText(QApplication::translate("tared", "Back", 0));
        label_2->setText(QApplication::translate("tared", "Tared.", 0));
    } // retranslateUi

};

namespace Ui {
    class tared: public Ui_tared {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TARED_H
