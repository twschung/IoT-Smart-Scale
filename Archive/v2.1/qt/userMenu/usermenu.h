#ifndef USERMENU_H
#define USERMENU_H

#include <QWidget>

namespace Ui {
class userMenu;
}

class userMenu : public QWidget
{
    Q_OBJECT

public:
    explicit userMenu(QWidget *parent = 0);
    ~userMenu();

private:
    Ui::userMenu *ui;
};

#endif // USERMENU_H
