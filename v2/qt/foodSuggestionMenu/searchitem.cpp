#include "searchitem.h"
#include "ui_searchitem.h"

searchItem::searchItem(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::searchItem)
{
    ui->setupUi(this);
}

searchItem::~searchItem()
{
    delete ui;
}
