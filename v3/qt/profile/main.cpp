#include "profile.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    profile w;
    w.show();

    return a.exec();
}
