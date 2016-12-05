#include "userinfo.h"
#include "ui_userinfo.h"

userInfo::userInfo(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::userInfo)
{
    ui->setupUi(this);
}

userInfo::~userInfo()
{
    delete ui;
}
