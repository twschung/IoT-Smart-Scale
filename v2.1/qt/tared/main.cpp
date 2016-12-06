#include "tared.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    tared w;
    w.show();

    return a.exec();
}
