#ifndef TRACKINGMENU_H
#define TRACKINGMENU_H

#include <QWidget>

namespace Ui {
class trackingMenu;
}

class trackingMenu : public QWidget
{
    Q_OBJECT

public:
    explicit trackingMenu(QWidget *parent = 0);
    ~trackingMenu();

private:
    Ui::trackingMenu *ui;
};

#endif // TRACKINGMENU_H
