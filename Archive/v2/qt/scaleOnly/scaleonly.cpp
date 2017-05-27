#include "scaleonly.h"
#include "ui_scaleonly.h"

scaleOnly::scaleOnly(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::scaleOnly)
{
    ui->setupUi(this);
}

scaleOnly::~scaleOnly()
{
    delete ui;
}
