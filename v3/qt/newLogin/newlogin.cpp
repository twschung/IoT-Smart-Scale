#include "newlogin.h"
#include "ui_newlogin.h"

newLogin::newLogin(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::newLogin)
{
    ui->setupUi(this);
}

newLogin::~newLogin()
{
    delete ui;
}
