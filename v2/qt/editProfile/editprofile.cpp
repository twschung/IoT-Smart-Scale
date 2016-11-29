#include "editprofile.h"
#include "ui_editprofile.h"

editProfile::editProfile(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::editProfile)
{
    ui->setupUi(this);
}

editProfile::~editProfile()
{
    delete ui;
}
