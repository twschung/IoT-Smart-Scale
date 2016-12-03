#ifndef NEWLOGIN_H
#define NEWLOGIN_H

#include <QWidget>

namespace Ui {
class newLogin;
}

class newLogin : public QWidget
{
    Q_OBJECT

public:
    explicit newLogin(QWidget *parent = 0);
    ~newLogin();

private:
    Ui::newLogin *ui;
};

#endif // NEWLOGIN_H
