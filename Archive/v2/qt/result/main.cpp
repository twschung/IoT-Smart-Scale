#include "result.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    result w;
    w.show();

    return a.exec();
}
