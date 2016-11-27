#ifndef PLACEFOOD_H
#define PLACEFOOD_H

#include <QDialog>

namespace Ui {
class placeFood;
}

class placeFood : public QDialog
{
    Q_OBJECT

public:
    explicit placeFood(QWidget *parent = 0);
    ~placeFood();

private:
    Ui::placeFood *ui;
};

#endif // PLACEFOOD_H
