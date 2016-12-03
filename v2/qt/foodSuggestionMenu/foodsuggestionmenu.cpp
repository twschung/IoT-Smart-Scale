#include "foodsuggestionmenu.h"
#include "ui_foodsuggestionmenu.h"

foodSuggestionMenu::foodSuggestionMenu(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::foodSuggestionMenu)
{
    ui->setupUi(this);
}

foodSuggestionMenu::~foodSuggestionMenu()
{
    delete ui;
}
