#ifndef MAINMENU_H
#define MAINMENU_H

#include <QWidget>
#include "loginmenu.h"
#include "foodinformation.h"
namespace Ui {
class mainMenu;
}

class mainMenu : public QWidget
{
    Q_OBJECT

public:
    explicit mainMenu(QWidget *parent = 0);
    ~mainMenu();

private slots:
    void on_btn_login_clicked();

    void on_btn_guest_clicked();

private:
    Ui::mainMenu *ui;
    loginMenu *loginmenu;
    foodInformation *foodinformation;
};

#endif // MAINMENU_H
