#ifndef USERSETUP_H
#define USERSETUP_H

#include <QWidget>

namespace Ui {
class userSetup;
}

class userSetup : public QWidget
{
    Q_OBJECT

public:
    explicit userSetup(QWidget *parent = 0);
    ~userSetup();

private:
    Ui::userSetup *ui;
};

#endif // USERSETUP_H
