#include "foodinformation.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    foodInformation w;
    w.show();

    return a.exec();
}
