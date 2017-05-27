#include "usersetup.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    userSetup w;
    w.show();

    return a.exec();
}
