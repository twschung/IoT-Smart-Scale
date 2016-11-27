#include "usersetup.h"
#include "ui_usersetup.h"

userSetup::userSetup(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::userSetup)
{
    ui->setupUi(this);
}

userSetup::~userSetup()
{
    delete ui;
}
