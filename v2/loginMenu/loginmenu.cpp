#include "loginmenu.h"
#include "ui_loginmenu.h"

loginMenu::loginMenu(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::loginMenu)
{
    ui->setupUi(this);
}

loginMenu::~loginMenu()
{
    delete ui;
}
