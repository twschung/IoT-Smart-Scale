#ifndef FORGOTPASSCODE_H
#define FORGOTPASSCODE_H

#include <QWidget>

namespace Ui {
class forgotPasscode;
}

class forgotPasscode : public QWidget
{
    Q_OBJECT

public:
    explicit forgotPasscode(QWidget *parent = 0);
    ~forgotPasscode();

private:
    Ui::forgotPasscode *ui;
};

#endif // FORGOTPASSCODE_H
