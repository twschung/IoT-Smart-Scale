#ifndef SEARCHITEM_H
#define SEARCHITEM_H

#include <QWidget>

namespace Ui {
class searchItem;
}

class searchItem : public QWidget
{
    Q_OBJECT

public:
    explicit searchItem(QWidget *parent = 0);
    ~searchItem();

private:
    Ui::searchItem *ui;
};

#endif // SEARCHITEM_H
