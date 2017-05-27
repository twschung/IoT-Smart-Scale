#ifndef FOODINFORMATION_H
#define FOODINFORMATION_H

#include <QWidget>

namespace Ui {
class foodInformation;
}

class foodInformation : public QWidget
{
    Q_OBJECT

public:
    explicit foodInformation(QWidget *parent = 0);
    ~foodInformation();

private:
    Ui::foodInformation *ui;
};

#endif // FOODINFORMATION_H
