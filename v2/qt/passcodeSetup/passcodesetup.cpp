#include "passcodesetup.h"
#include "ui_passcodesetup.h"

passcodeSetup::passcodeSetup(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::passcodeSetup)
{
    ui->setupUi(this);
}

passcodeSetup::~passcodeSetup()
{
    delete ui;
}
