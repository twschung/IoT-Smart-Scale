#include "trackingmenu.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    trackingMenu w;
    w.show();

    return a.exec();
}
