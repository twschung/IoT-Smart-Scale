#include "searchitem.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    searchItem w;
    w.show();

    return a.exec();
}
