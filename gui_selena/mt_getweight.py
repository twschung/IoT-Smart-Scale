# -*- coding: utf-8 -*-
import sys, time, os

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime

import ui_getWeight, ui_itemSuggestion

#from hx711 import HX711

class GetWeightWindow(QMainWindow, ui_getWeight.Ui_getWeight):
    def __init__(self): #, currentUser removed
        super (self.__class__, self).__init__()
        self.setupUi(self)
        self.btnScan.clicked.connect(lambda:self.btnScan_pressed())
        self.btnTare.clicked.connect(lambda:self.btnTare_pressed())
        self.thread1 = get_weight_thread()
        self.thread1.start()
    def btnTare_pressed(self):
        scale.tare()
        self.weight = scale.get_weight(5)
        self.lcdWeight.display(int(self.weight))
    def btnScan_pressed(self):
        self.weight = scale.get_weight(5)
        self.lcdWeight.display(int(self.weight))

class get_weight_thread (QThread):
    def __init__(self):
        QThread.__init__(self)
        print ("Initialise Thread")
    def run(self):
        print ("Starting Thread")
        self._get_weight_1()
        print ("Exiting Thread")
    def _get_weight_1(self):
        while True:
            self.val = int(scale.get_weight(5))
            print ("current reading = " + str(self.val)+"g")
            GetWeightWindow.lcdWeight.display(int(self.val))
        
def main():
    app = QApplication(sys.argv)
    currentForm = GetWeightWindow()
    currentForm.show()
    sys.exit(app.exec_())

def userGetWeight(self):
    self.close()
    currentForm = GetWeightWindow()
    currentForm.showMaximized()

if __name__ == "__main__":
    '''
    scale = HX711(23,24)
    scale.set_reference_unit(770)
    scale.reset()
    scale.tare()
    '''
    main()

