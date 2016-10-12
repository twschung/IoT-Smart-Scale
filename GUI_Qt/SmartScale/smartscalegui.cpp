#include "smartscalegui.h"
#include "ui_smartscalegui.h"

smartScaleGUI::smartScaleGUI(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::smartScaleGUI)
{
    ui->setupUi(this);
}

smartScaleGUI::~smartScaleGUI()
{
    delete ui;
}
