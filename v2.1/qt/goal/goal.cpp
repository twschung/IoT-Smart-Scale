#include "goal.h"
#include "ui_goal.h"

goal::goal(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::goal)
{
    ui->setupUi(this);
}

goal::~goal()
{
    delete ui;
}
