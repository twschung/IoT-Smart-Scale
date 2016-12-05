#include "passcode.h"
#include "ui_passcode.h"

passCode::passCode(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::passCode)
{
    ui->setupUi(this);
}

passCode::~passCode()
{
    delete ui;
}
