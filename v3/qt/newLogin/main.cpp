#include "newlogin.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    newLogin w;
    w.show();

    return a.exec();
}
