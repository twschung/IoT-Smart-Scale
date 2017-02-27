#ifndef PASSCODESETUP_H
#define PASSCODESETUP_H

#include <QWidget>

namespace Ui {
class passcodeSetup;
}

class passcodeSetup : public QWidget
{
    Q_OBJECT

public:
    explicit passcodeSetup(QWidget *parent = 0);
    ~passcodeSetup();

private:
    Ui::passcodeSetup *ui;
};

#endif // PASSCODESETUP_H
