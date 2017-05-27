#include "smartscalegui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    smartScaleGUI w;
    w.show();

    return a.exec();
}
