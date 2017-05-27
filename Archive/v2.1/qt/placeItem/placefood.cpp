#include "placefood.h"
#include "ui_placefood.h"

placeFood::placeFood(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::placeFood)
{
    ui->setupUi(this);
}

placeFood::~placeFood()
{
    delete ui;
}
