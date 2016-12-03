#ifndef SCALEONLY_H
#define SCALEONLY_H

#include <QWidget>

namespace Ui {
class scaleOnly;
}

class scaleOnly : public QWidget
{
    Q_OBJECT

public:
    explicit scaleOnly(QWidget *parent = 0);
    ~scaleOnly();

private:
    Ui::scaleOnly *ui;
};

#endif // SCALEONLY_H
