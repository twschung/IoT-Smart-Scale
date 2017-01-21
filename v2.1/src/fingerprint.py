import myInfoPopUp
from pyfingerprint import PyFingerprint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

def connectToFingerPrint():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')
        else:
            return f
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

def enrollFinger(self,currentPositionNumber=None):
    f = connectToFingerPrint()
    try:
        msgbox = myInfoPopUp.myInfoPopUp("Place finger...", "Please place finger on scanner",self)
		msgbox.exec_()
        while ( f.readImage() == False ):
            pass
        msgbox.done(1)
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        if ( positionNumber >= 0 ):
            QMessageBox.information(self, 'Error',"Finger already registered",QMessageBox.Ok)
            return (False, 2)
        else:
            msgbox = myInfoPopUp.myInfoPopUp("Remove finger...", "Please remove finger from scanner",self)
    		msgbox.exec_()
            time.sleep(2)
            msgbox.done(1)
            msgbox = myInfoPopUp.myInfoPopUp("Place finger...", "Please place the same finger on scanner",self)
            msgbox.exec_()
            while ( f.readImage() == False ):
                pass
            msgbox.done(1)
            f.convertImage(0x02)
            if f.compareCharacteristics() != 0:
                f.createTemplate()
                positionNumber = f.storeTemplate()
                QMessageBox.information(self, 'Success',"Finger enrolled successfully",QMessageBox.Ok)
                if (currentPositionNumber is not None):
                    f.deleteTemplate(int(currentPositionNumber))
                return (True, positionNumber)
            else:
                QMessageBox.information(self, 'Error',"Finger not match",QMessageBox.Ok)
                return (False, 1)
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        return (False, 0)
