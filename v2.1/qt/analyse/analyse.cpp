#include "analyse.h"
#include "ui_analyse.h"

analyse::analyse(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::analyse)
{
    ui->setupUi(this);
}

analyse::~analyse()
{
    delete ui;
}
