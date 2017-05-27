/********************************************************************************
** Form generated from reading UI file 'newlogin.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_NEWLOGIN_H
#define UI_NEWLOGIN_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_newLogin
{
public:
    QGridLayout *gridLayout;
    QPushButton *btn_login;
    QPushButton *btn_back;
    QLabel *lbl_title;
    QSpacerItem *horizontalSpacer;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_2;
    QFrame *keyboard;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *row1;
    QPushButton *Q;
    QPushButton *W;
    QPushButton *E;
    QPushButton *R;
    QPushButton *T;
    QPushButton *Y;
    QPushButton *U;
    QPushButton *I;
    QPushButton *O;
    QPushButton *P;
    QHBoxLayout *row2;
    QPushButton *A;
    QPushButton *S;
    QPushButton *D;
    QPushButton *F;
    QPushButton *G;
    QPushButton *H;
    QPushButton *J;
    QPushButton *K;
    QPushButton *L;
    QHBoxLayout *row3;
    QPushButton *btnShift;
    QPushButton *Z;
    QPushButton *X;
    QPushButton *C;
    QPushButton *V;
    QPushButton *B;
    QPushButton *N;
    QPushButton *M;
    QPushButton *btnDel;
    QHBoxLayout *row4;
    QPushButton *btnToggle;
    QPushButton *space;
    QPushButton *btnAt;
    QPushButton *btnDot;
    QPushButton *btnReturn;
    QSpacerItem *verticalSpacer;
    QLabel *lbl_email;
    QLineEdit *lineEdit_email;
    QSpacerItem *horizontalSpacer_2;

    void setupUi(QWidget *newLogin)
    {
        if (newLogin->objectName().isEmpty())
            newLogin->setObjectName(QStringLiteral("newLogin"));
        newLogin->resize(800, 480);
        QFont font;
        font.setFamily(QStringLiteral("Arial"));
        font.setPointSize(11);
        newLogin->setFont(font);
        gridLayout = new QGridLayout(newLogin);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        btn_login = new QPushButton(newLogin);
        btn_login->setObjectName(QStringLiteral("btn_login"));
        btn_login->setMinimumSize(QSize(141, 71));
        QFont font1;
        font1.setFamily(QStringLiteral("Helvetica Neue"));
        font1.setPointSize(16);
        btn_login->setFont(font1);

        gridLayout->addWidget(btn_login, 2, 2, 1, 1);

        btn_back = new QPushButton(newLogin);
        btn_back->setObjectName(QStringLiteral("btn_back"));
        btn_back->setMinimumSize(QSize(141, 71));
        btn_back->setFont(font1);

        gridLayout->addWidget(btn_back, 2, 0, 1, 1);

        lbl_title = new QLabel(newLogin);
        lbl_title->setObjectName(QStringLiteral("lbl_title"));
        lbl_title->setMinimumSize(QSize(121, 31));
        QFont font2;
        font2.setFamily(QStringLiteral("Helvetica Neue"));
        font2.setPointSize(24);
        font2.setBold(true);
        font2.setWeight(75);
        lbl_title->setFont(font2);

        gridLayout->addWidget(lbl_title, 0, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(487, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 2, 1, 1, 1);

        groupBox = new QGroupBox(newLogin);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setMinimumSize(QSize(741, 331));
        gridLayout_2 = new QGridLayout(groupBox);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        keyboard = new QFrame(groupBox);
        keyboard->setObjectName(QStringLiteral("keyboard"));
        keyboard->setMaximumSize(QSize(510, 250));
        keyboard->setFrameShape(QFrame::StyledPanel);
        keyboard->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(keyboard);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        row1 = new QHBoxLayout();
        row1->setSpacing(6);
        row1->setObjectName(QStringLiteral("row1"));
        Q = new QPushButton(keyboard);
        Q->setObjectName(QStringLiteral("Q"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Q->sizePolicy().hasHeightForWidth());
        Q->setSizePolicy(sizePolicy);
        Q->setMinimumSize(QSize(46, 46));
        Q->setMaximumSize(QSize(46, 46));

        row1->addWidget(Q);

        W = new QPushButton(keyboard);
        W->setObjectName(QStringLiteral("W"));
        sizePolicy.setHeightForWidth(W->sizePolicy().hasHeightForWidth());
        W->setSizePolicy(sizePolicy);
        W->setMinimumSize(QSize(46, 46));
        W->setMaximumSize(QSize(46, 46));

        row1->addWidget(W);

        E = new QPushButton(keyboard);
        E->setObjectName(QStringLiteral("E"));
        sizePolicy.setHeightForWidth(E->sizePolicy().hasHeightForWidth());
        E->setSizePolicy(sizePolicy);
        E->setMinimumSize(QSize(46, 46));
        E->setMaximumSize(QSize(46, 46));

        row1->addWidget(E);

        R = new QPushButton(keyboard);
        R->setObjectName(QStringLiteral("R"));
        sizePolicy.setHeightForWidth(R->sizePolicy().hasHeightForWidth());
        R->setSizePolicy(sizePolicy);
        R->setMinimumSize(QSize(46, 46));
        R->setMaximumSize(QSize(46, 46));

        row1->addWidget(R);

        T = new QPushButton(keyboard);
        T->setObjectName(QStringLiteral("T"));
        sizePolicy.setHeightForWidth(T->sizePolicy().hasHeightForWidth());
        T->setSizePolicy(sizePolicy);
        T->setMinimumSize(QSize(46, 46));
        T->setMaximumSize(QSize(46, 46));

        row1->addWidget(T);

        Y = new QPushButton(keyboard);
        Y->setObjectName(QStringLiteral("Y"));
        sizePolicy.setHeightForWidth(Y->sizePolicy().hasHeightForWidth());
        Y->setSizePolicy(sizePolicy);
        Y->setMinimumSize(QSize(46, 46));
        Y->setMaximumSize(QSize(46, 46));

        row1->addWidget(Y);

        U = new QPushButton(keyboard);
        U->setObjectName(QStringLiteral("U"));
        sizePolicy.setHeightForWidth(U->sizePolicy().hasHeightForWidth());
        U->setSizePolicy(sizePolicy);
        U->setMinimumSize(QSize(46, 46));
        U->setMaximumSize(QSize(46, 46));

        row1->addWidget(U);

        I = new QPushButton(keyboard);
        I->setObjectName(QStringLiteral("I"));
        sizePolicy.setHeightForWidth(I->sizePolicy().hasHeightForWidth());
        I->setSizePolicy(sizePolicy);
        I->setMinimumSize(QSize(46, 46));
        I->setMaximumSize(QSize(46, 46));

        row1->addWidget(I);

        O = new QPushButton(keyboard);
        O->setObjectName(QStringLiteral("O"));
        sizePolicy.setHeightForWidth(O->sizePolicy().hasHeightForWidth());
        O->setSizePolicy(sizePolicy);
        O->setMinimumSize(QSize(46, 46));
        O->setMaximumSize(QSize(46, 46));

        row1->addWidget(O);

        P = new QPushButton(keyboard);
        P->setObjectName(QStringLiteral("P"));
        sizePolicy.setHeightForWidth(P->sizePolicy().hasHeightForWidth());
        P->setSizePolicy(sizePolicy);
        P->setMinimumSize(QSize(46, 46));
        P->setMaximumSize(QSize(46, 46));

        row1->addWidget(P);


        verticalLayout->addLayout(row1);

        row2 = new QHBoxLayout();
        row2->setSpacing(6);
        row2->setObjectName(QStringLiteral("row2"));
        A = new QPushButton(keyboard);
        A->setObjectName(QStringLiteral("A"));
        sizePolicy.setHeightForWidth(A->sizePolicy().hasHeightForWidth());
        A->setSizePolicy(sizePolicy);
        A->setMinimumSize(QSize(46, 46));
        A->setMaximumSize(QSize(46, 46));

        row2->addWidget(A);

        S = new QPushButton(keyboard);
        S->setObjectName(QStringLiteral("S"));
        sizePolicy.setHeightForWidth(S->sizePolicy().hasHeightForWidth());
        S->setSizePolicy(sizePolicy);
        S->setMinimumSize(QSize(46, 46));
        S->setMaximumSize(QSize(46, 46));

        row2->addWidget(S);

        D = new QPushButton(keyboard);
        D->setObjectName(QStringLiteral("D"));
        sizePolicy.setHeightForWidth(D->sizePolicy().hasHeightForWidth());
        D->setSizePolicy(sizePolicy);
        D->setMinimumSize(QSize(46, 46));
        D->setMaximumSize(QSize(46, 46));

        row2->addWidget(D);

        F = new QPushButton(keyboard);
        F->setObjectName(QStringLiteral("F"));
        sizePolicy.setHeightForWidth(F->sizePolicy().hasHeightForWidth());
        F->setSizePolicy(sizePolicy);
        F->setMinimumSize(QSize(46, 46));
        F->setMaximumSize(QSize(46, 46));

        row2->addWidget(F);

        G = new QPushButton(keyboard);
        G->setObjectName(QStringLiteral("G"));
        sizePolicy.setHeightForWidth(G->sizePolicy().hasHeightForWidth());
        G->setSizePolicy(sizePolicy);
        G->setMinimumSize(QSize(46, 46));
        G->setMaximumSize(QSize(46, 46));

        row2->addWidget(G);

        H = new QPushButton(keyboard);
        H->setObjectName(QStringLiteral("H"));
        sizePolicy.setHeightForWidth(H->sizePolicy().hasHeightForWidth());
        H->setSizePolicy(sizePolicy);
        H->setMinimumSize(QSize(46, 46));
        H->setMaximumSize(QSize(46, 46));

        row2->addWidget(H);

        J = new QPushButton(keyboard);
        J->setObjectName(QStringLiteral("J"));
        sizePolicy.setHeightForWidth(J->sizePolicy().hasHeightForWidth());
        J->setSizePolicy(sizePolicy);
        J->setMinimumSize(QSize(46, 46));
        J->setMaximumSize(QSize(46, 46));

        row2->addWidget(J);

        K = new QPushButton(keyboard);
        K->setObjectName(QStringLiteral("K"));
        sizePolicy.setHeightForWidth(K->sizePolicy().hasHeightForWidth());
        K->setSizePolicy(sizePolicy);
        K->setMinimumSize(QSize(46, 46));
        K->setMaximumSize(QSize(46, 46));

        row2->addWidget(K);

        L = new QPushButton(keyboard);
        L->setObjectName(QStringLiteral("L"));
        sizePolicy.setHeightForWidth(L->sizePolicy().hasHeightForWidth());
        L->setSizePolicy(sizePolicy);
        L->setMinimumSize(QSize(46, 46));
        L->setMaximumSize(QSize(46, 46));

        row2->addWidget(L);


        verticalLayout->addLayout(row2);

        row3 = new QHBoxLayout();
        row3->setSpacing(6);
        row3->setObjectName(QStringLiteral("row3"));
        btnShift = new QPushButton(keyboard);
        btnShift->setObjectName(QStringLiteral("btnShift"));
        sizePolicy.setHeightForWidth(btnShift->sizePolicy().hasHeightForWidth());
        btnShift->setSizePolicy(sizePolicy);
        btnShift->setMinimumSize(QSize(0, 46));
        btnShift->setMaximumSize(QSize(49, 46));

        row3->addWidget(btnShift);

        Z = new QPushButton(keyboard);
        Z->setObjectName(QStringLiteral("Z"));
        sizePolicy.setHeightForWidth(Z->sizePolicy().hasHeightForWidth());
        Z->setSizePolicy(sizePolicy);
        Z->setMinimumSize(QSize(46, 46));
        Z->setMaximumSize(QSize(46, 46));

        row3->addWidget(Z);

        X = new QPushButton(keyboard);
        X->setObjectName(QStringLiteral("X"));
        sizePolicy.setHeightForWidth(X->sizePolicy().hasHeightForWidth());
        X->setSizePolicy(sizePolicy);
        X->setMinimumSize(QSize(46, 46));
        X->setMaximumSize(QSize(46, 46));

        row3->addWidget(X);

        C = new QPushButton(keyboard);
        C->setObjectName(QStringLiteral("C"));
        sizePolicy.setHeightForWidth(C->sizePolicy().hasHeightForWidth());
        C->setSizePolicy(sizePolicy);
        C->setMinimumSize(QSize(46, 46));
        C->setMaximumSize(QSize(46, 46));

        row3->addWidget(C);

        V = new QPushButton(keyboard);
        V->setObjectName(QStringLiteral("V"));
        sizePolicy.setHeightForWidth(V->sizePolicy().hasHeightForWidth());
        V->setSizePolicy(sizePolicy);
        V->setMinimumSize(QSize(46, 46));
        V->setMaximumSize(QSize(46, 46));

        row3->addWidget(V);

        B = new QPushButton(keyboard);
        B->setObjectName(QStringLiteral("B"));
        sizePolicy.setHeightForWidth(B->sizePolicy().hasHeightForWidth());
        B->setSizePolicy(sizePolicy);
        B->setMinimumSize(QSize(46, 46));
        B->setMaximumSize(QSize(46, 46));

        row3->addWidget(B);

        N = new QPushButton(keyboard);
        N->setObjectName(QStringLiteral("N"));
        sizePolicy.setHeightForWidth(N->sizePolicy().hasHeightForWidth());
        N->setSizePolicy(sizePolicy);
        N->setMinimumSize(QSize(46, 46));
        N->setMaximumSize(QSize(46, 46));

        row3->addWidget(N);

        M = new QPushButton(keyboard);
        M->setObjectName(QStringLiteral("M"));
        sizePolicy.setHeightForWidth(M->sizePolicy().hasHeightForWidth());
        M->setSizePolicy(sizePolicy);
        M->setMinimumSize(QSize(46, 46));
        M->setMaximumSize(QSize(46, 46));

        row3->addWidget(M);

        btnDel = new QPushButton(keyboard);
        btnDel->setObjectName(QStringLiteral("btnDel"));
        sizePolicy.setHeightForWidth(btnDel->sizePolicy().hasHeightForWidth());
        btnDel->setSizePolicy(sizePolicy);
        btnDel->setMinimumSize(QSize(0, 46));
        btnDel->setMaximumSize(QSize(49, 46));

        row3->addWidget(btnDel);


        verticalLayout->addLayout(row3);

        row4 = new QHBoxLayout();
        row4->setSpacing(6);
        row4->setObjectName(QStringLiteral("row4"));
        btnToggle = new QPushButton(keyboard);
        btnToggle->setObjectName(QStringLiteral("btnToggle"));
        btnToggle->setMinimumSize(QSize(0, 46));
        btnToggle->setMaximumSize(QSize(16777215, 46));

        row4->addWidget(btnToggle);

        space = new QPushButton(keyboard);
        space->setObjectName(QStringLiteral("space"));
        space->setMinimumSize(QSize(200, 46));
        space->setMaximumSize(QSize(16777215, 46));

        row4->addWidget(space);

        btnAt = new QPushButton(keyboard);
        btnAt->setObjectName(QStringLiteral("btnAt"));
        btnAt->setMinimumSize(QSize(0, 46));
        btnAt->setMaximumSize(QSize(16777215, 46));

        row4->addWidget(btnAt);

        btnDot = new QPushButton(keyboard);
        btnDot->setObjectName(QStringLiteral("btnDot"));
        btnDot->setMinimumSize(QSize(0, 46));
        btnDot->setMaximumSize(QSize(16777215, 46));

        row4->addWidget(btnDot);

        btnReturn = new QPushButton(keyboard);
        btnReturn->setObjectName(QStringLiteral("btnReturn"));
        btnReturn->setMinimumSize(QSize(0, 46));
        btnReturn->setMaximumSize(QSize(16777215, 46));

        row4->addWidget(btnReturn);


        verticalLayout->addLayout(row4);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);


        gridLayout_2->addWidget(keyboard, 1, 1, 1, 1);

        lbl_email = new QLabel(groupBox);
        lbl_email->setObjectName(QStringLiteral("lbl_email"));
        lbl_email->setMinimumSize(QSize(50, 20));
        QFont font3;
        font3.setFamily(QStringLiteral("Helvetica Neue"));
        font3.setPointSize(16);
        font3.setBold(true);
        font3.setWeight(75);
        lbl_email->setFont(font3);

        gridLayout_2->addWidget(lbl_email, 0, 0, 1, 1);

        lineEdit_email = new QLineEdit(groupBox);
        lineEdit_email->setObjectName(QStringLiteral("lineEdit_email"));
        lineEdit_email->setMinimumSize(QSize(513, 19));

        gridLayout_2->addWidget(lineEdit_email, 0, 1, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(10000, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 1, 2, 1, 1);


        gridLayout->addWidget(groupBox, 1, 0, 1, 3);


        retranslateUi(newLogin);

        QMetaObject::connectSlotsByName(newLogin);
    } // setupUi

    void retranslateUi(QWidget *newLogin)
    {
        newLogin->setWindowTitle(QApplication::translate("newLogin", "newLogin", 0));
        btn_login->setText(QApplication::translate("newLogin", "Login", 0));
        btn_back->setText(QApplication::translate("newLogin", "Back", 0));
        lbl_title->setText(QApplication::translate("newLogin", "New Login", 0));
        groupBox->setTitle(QString());
        Q->setText(QApplication::translate("newLogin", "Q", 0));
        W->setText(QApplication::translate("newLogin", "W", 0));
        E->setText(QApplication::translate("newLogin", "E", 0));
        R->setText(QApplication::translate("newLogin", "R", 0));
        T->setText(QApplication::translate("newLogin", "T", 0));
        Y->setText(QApplication::translate("newLogin", "Y", 0));
        U->setText(QApplication::translate("newLogin", "U", 0));
        I->setText(QApplication::translate("newLogin", "I", 0));
        O->setText(QApplication::translate("newLogin", "O", 0));
        P->setText(QApplication::translate("newLogin", "P", 0));
        A->setText(QApplication::translate("newLogin", "A", 0));
        S->setText(QApplication::translate("newLogin", "S", 0));
        D->setText(QApplication::translate("newLogin", "D", 0));
        F->setText(QApplication::translate("newLogin", "F", 0));
        G->setText(QApplication::translate("newLogin", "G", 0));
        H->setText(QApplication::translate("newLogin", "H", 0));
        J->setText(QApplication::translate("newLogin", "J", 0));
        K->setText(QApplication::translate("newLogin", "K", 0));
        L->setText(QApplication::translate("newLogin", "L", 0));
        btnShift->setText(QApplication::translate("newLogin", "Shift", 0));
        Z->setText(QApplication::translate("newLogin", "Z", 0));
        X->setText(QApplication::translate("newLogin", "X", 0));
        C->setText(QApplication::translate("newLogin", "C", 0));
        V->setText(QApplication::translate("newLogin", "V", 0));
        B->setText(QApplication::translate("newLogin", "B", 0));
        N->setText(QApplication::translate("newLogin", "N", 0));
        M->setText(QApplication::translate("newLogin", "M", 0));
        btnDel->setText(QApplication::translate("newLogin", "Del", 0));
        btnToggle->setText(QApplication::translate("newLogin", "123", 0));
        space->setText(QApplication::translate("newLogin", "space", 0));
        btnAt->setText(QApplication::translate("newLogin", "@", 0));
        btnDot->setText(QApplication::translate("newLogin", ".", 0));
        btnReturn->setText(QApplication::translate("newLogin", "return", 0));
        lbl_email->setText(QApplication::translate("newLogin", "Email:", 0));
    } // retranslateUi

};

namespace Ui {
    class newLogin: public Ui_newLogin {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_NEWLOGIN_H
