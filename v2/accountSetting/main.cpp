#include "accountsetting.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    accountSetting w;
    w.show();

    return a.exec();
}
