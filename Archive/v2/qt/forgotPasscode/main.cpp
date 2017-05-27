#include "forgotpasscode.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    forgotPasscode w;
    w.show();

    return a.exec();
}
