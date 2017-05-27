#ifndef FOODSUGGESTIONMENU_H
#define FOODSUGGESTIONMENU_H

#include <QWidget>

namespace Ui {
class foodSuggestionMenu;
}

class foodSuggestionMenu : public QWidget
{
    Q_OBJECT

public:
    explicit foodSuggestionMenu(QWidget *parent = 0);
    ~foodSuggestionMenu();

private:
    Ui::foodSuggestionMenu *ui;
};

#endif // FOODSUGGESTIONMENU_H
