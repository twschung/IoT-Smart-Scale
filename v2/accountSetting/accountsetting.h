#ifndef ACCOUNTSETTING_H
#define ACCOUNTSETTING_H

#include <QWidget>

namespace Ui {
class accountSetting;
}

class accountSetting : public QWidget
{
    Q_OBJECT

public:
    explicit accountSetting(QWidget *parent = 0);
    ~accountSetting();

private:
    Ui::accountSetting *ui;
};

#endif // ACCOUNTSETTING_H
