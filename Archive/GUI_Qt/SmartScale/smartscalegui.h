#ifndef SMARTSCALEGUI_H
#define SMARTSCALEGUI_H

#include <QMainWindow>

namespace Ui {
class smartScaleGUI;
}

class smartScaleGUI : public QMainWindow
{
    Q_OBJECT

public:
    explicit smartScaleGUI(QWidget *parent = 0);
    ~smartScaleGUI();

private:
    Ui::smartScaleGUI *ui;
};

#endif // SMARTSCALEGUI_H
