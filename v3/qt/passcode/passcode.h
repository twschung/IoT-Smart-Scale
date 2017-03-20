#ifndef PASSCODE_H
#define PASSCODE_H

#include <QWidget>

namespace Ui {
class passCode;
}

class passCode : public QWidget
{
    Q_OBJECT

public:
    explicit passCode(QWidget *parent = 0);
    ~passCode();

private:
    Ui::passCode *ui;
};

#endif // PASSCODE_H
