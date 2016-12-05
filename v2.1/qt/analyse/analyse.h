#ifndef ANALYSE_H
#define ANALYSE_H

#include <QWidget>

namespace Ui {
class analyse;
}

class analyse : public QWidget
{
    Q_OBJECT

public:
    explicit analyse(QWidget *parent = 0);
    ~analyse();

private:
    Ui::analyse *ui;
};

#endif // ANALYSE_H
