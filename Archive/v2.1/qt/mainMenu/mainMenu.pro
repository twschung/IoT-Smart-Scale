#-------------------------------------------------
#
# Project created by QtCreator 2016-11-22T15:20:42
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = mainMenu
TEMPLATE = app


SOURCES += main.cpp\
        mainmenu.cpp \
    loginmenu.cpp \
    foodinformation.cpp

HEADERS  += mainmenu.h \
    loginmenu.h \
    foodinformation.h

FORMS    += mainmenu.ui \
    loginmenu.ui \
    foodinformation.ui
