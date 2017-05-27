#include "usermenu.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    userMenu w;
    w.show();

    return a.exec();
}
