#ifndef EDITPROFILE_H
#define EDITPROFILE_H

#include <QDialog>

namespace Ui {
class editProfile;
}

class editProfile : public QDialog
{
    Q_OBJECT

public:
    explicit editProfile(QWidget *parent = 0);
    ~editProfile();

private:
    Ui::editProfile *ui;
};

#endif // EDITPROFILE_H
