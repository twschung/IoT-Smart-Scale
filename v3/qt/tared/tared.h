#ifndef TARED_H
#define TARED_H

#include <QDialog>

namespace Ui {
class tared;
}

class tared : public QDialog
{
    Q_OBJECT

public:
    explicit tared(QWidget *parent = 0);
    ~tared();

private:
    Ui::tared *ui;
};

#endif // TARED_H
