#include "trackingmenu.h"
#include "ui_trackingmenu.h"

trackingMenu::trackingMenu(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::trackingMenu)
{
    ui->setupUi(this);
}

trackingMenu::~trackingMenu()
{
    delete ui;
}
