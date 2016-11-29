#include "foodsuggestionmenu.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    foodSuggestionMenu w;
    w.show();

    return a.exec();
}
