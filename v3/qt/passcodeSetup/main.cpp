#include "passcodesetup.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    passcodeSetup w;
    w.show();

    return a.exec();
}
