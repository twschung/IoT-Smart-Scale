#include "foodinformation.h"
#include "ui_foodinformation.h"

foodInformation::foodInformation(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::foodInformation)
{
    ui->setupUi(this);
}

foodInformation::~foodInformation()
{
    delete ui;
}
