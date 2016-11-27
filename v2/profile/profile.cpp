#include "profile.h"
#include "ui_profile.h"

profile::profile(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::profile)
{
    ui->setupUi(this);
}

profile::~profile()
{
    delete ui;
}
