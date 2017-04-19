#include "mainmenu.h"
#include "ui_mainmenu.h"

mainMenu::mainMenu(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::mainMenu)
{
    ui->setupUi(this);
}

mainMenu::~mainMenu()
{
    delete ui;
}

void mainMenu::on_btn_login_clicked()
{
    //hide();
    loginmenu = new loginMenu(this);
    loginmenu->show();
}

void mainMenu::on_btn_guest_clicked()
{
    this->hide();
    foodinformation = new foodInformation(this);
    foodinformation->show();
}
