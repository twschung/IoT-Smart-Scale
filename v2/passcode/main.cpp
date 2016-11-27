#include "passcode.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    passCode w;
    w.show();

    return a.exec();
}
