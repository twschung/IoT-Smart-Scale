#ifndef GOAL_H
#define GOAL_H

#include <QWidget>

namespace Ui {
class goal;
}

class goal : public QWidget
{
    Q_OBJECT

public:
    explicit goal(QWidget *parent = 0);
    ~goal();

private:
    Ui::goal *ui;
};

#endif // GOAL_H
