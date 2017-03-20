#include "tared.h"
#include "ui_tared.h"

tared::tared(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::tared)
{
    ui->setupUi(this);
}

tared::~tared()
{
    delete ui;
}
