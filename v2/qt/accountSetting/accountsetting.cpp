#include "accountsetting.h"
#include "ui_accountsetting.h"

accountSetting::accountSetting(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::accountSetting)
{
    ui->setupUi(this);
}

accountSetting::~accountSetting()
{
    delete ui;
}
