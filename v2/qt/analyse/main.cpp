#include "analyse.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    analyse w;
    w.show();

    return a.exec();
}
