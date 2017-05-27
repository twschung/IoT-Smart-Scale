#include "usermenu.h"
#include "ui_usermenu.h"

userMenu::userMenu(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::userMenu)
{
    ui->setupUi(this);
}

userMenu::~userMenu()
{
    delete ui;
}
