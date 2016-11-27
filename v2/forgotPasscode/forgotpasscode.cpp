#include "forgotpasscode.h"
#include "ui_forgotpasscode.h"

forgotPasscode::forgotPasscode(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::forgotPasscode)
{
    ui->setupUi(this);
}

forgotPasscode::~forgotPasscode()
{
    delete ui;
}
