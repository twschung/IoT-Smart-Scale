#ifndef LOGINMENU_H
#define LOGINMENU_H

#include <QWidget>

namespace Ui {
class loginMenu;
}

class loginMenu : public QWidget
{
    Q_OBJECT

public:
    explicit loginMenu(QWidget *parent = 0);
    ~loginMenu();

private:
    Ui::loginMenu *ui;
};

#endif // LOGINMENU_H
