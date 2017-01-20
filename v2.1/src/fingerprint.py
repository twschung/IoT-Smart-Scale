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

def enrollNewFinger(self):
    f = connectToFingerPrint()
    try:
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setText("Please place finger on scanner")
        msgbox.setWindowModality(Qt.NonModal)
        QCoreApplication.processEvents()
        msgbox.show()
        QCoreApplication.processEvents()
        while ( f.readImage() == False ):
            pass
        msgbox.done(1)
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        if ( positionNumber >= 0 ):
            return (False, 2)
        else:
            print('Remove finger...')
            time.sleep(2)
            print('Waiting for same finger again...')

            while ( f.readImage() == False ):
                pass
            f.convertImage(0x02)
            if f.compareCharacteristics() != 0:
                f.createTemplate()
                positionNumber = f.storeTemplate()
                print('Finger enrolled successfully!')
                return (True, positionNumber)
            else:
                print('Fingerprints do not match')
                return (False, 1)
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        return (False, 0)
