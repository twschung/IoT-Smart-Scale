#include "scaleonly.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    scaleOnly w;
    w.show();

    return a.exec();
}
