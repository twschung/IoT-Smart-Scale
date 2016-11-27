#include "placefood.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    placeFood w;
    w.show();

    return a.exec();
}
