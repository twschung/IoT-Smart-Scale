import sys
sys.path.insert(0,"/home/pi/Desktop/v2.1/src")
sys.path.insert(0,"/home/pi/Desktop/v2.1/ui")
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui_foodinformation
import db_access, db_structure
import time

from hx711 import HX711

class myFoodInformation(QWidget, ui_foodinformation.Ui_foodInformation):
	def __init__(self, mainWindow, currentUserInfo, name=None, layoutSetting=None):
		super(myFoodInformation, self).__init__()
		self.setupUi(self)
		self.foodInfo = None
		userDailyIntakeInfo = db_structure.userDailyIntakeStructure()
		self.btn_new.setText("Scan")
		if (layoutSetting == "guest"):
			self.btn_addIntake.setEnabled(False)
		self.btn_back.clicked.connect(lambda:self.handleBtn_back(mainWindow))
		self.btn_new.clicked.connect(lambda:self.handleBtn_scan(mainWindow,currentUserInfo))
		self.btn_tare.clicked.connect(lambda:self.handleBtn_tare(mainWindow))
		self.btn_addIntake.setEnabled(False)
		self.btn_addIntake.clicked.connect(lambda:self.handleBtn_addIntake())

		# set up thread that will update weight
		self.thread = QThread()
		self.getWeight = get_weight_thread()
		self.getWeight.finished[int].connect(self.onFinished)
		self.getWeight.moveToThread(self.thread)
		self.thread.started.connect(self.getWeight.work)
		self.thread.start()	
	
	@pyqtSlot(int)
	def onFinished(self, i):
		self.lcd_number.display(int(i))

	def handleBtn_back(self,mainWindow):
		mainWindow.central_widget.removeWidget(mainWindow.central_widget.currentWidget())
	def handleBtn_scan(self,mainWindow,currentUserInfo):
		# add camera modules stuff here
		self.btn_addIntake.setEnabled(False)
		if(currentUserInfo==None):
			userId=0
		else:
			userId=currentUserInfo.id
		self.foodInfo = db_access.food_getActualInfo(userId,1,100)
		self.lbl_evergyVal.setText(str(self.foodInfo.energy)) #typo on the ui file, use 'evergy'
		self.lbl_proteinVal.setText(str(self.foodInfo.protein))
		self.lbl_sugarVal.setText(str(self.foodInfo.sugars))
		self.lbl_fibreVal.setText(str(self.foodInfo.fibre))
		self.lbl_fatVal.setText(str(self.foodInfo.fat))
		self.lbl_saltVal.setText(str(self.foodInfo.salt))
		if(currentUserInfo==None):
			self.btn_addIntake.setEnabled(False)
		else:
			self.btn_addIntake.setEnabled(True)
	def handleBtn_tare(self, mainWindow):
		# add tare stuff here
		scale.tare()
	def handleBtn_addIntake(self):
		db_access.user_addNewFoodIntake(self.foodInfo)
		msg = QMessageBox.information(self, 'Added',"Food item has been added to your intake",QMessageBox.Ok)
		self.btn_addIntake.setEnabled(False)

class get_weight_thread (QObject):
	finished = pyqtSignal(int)

	def __init__(self):
		print ("get_weight_thread init")
		#super (self.__class__, self).__init__()
		super().__init__()

	def work(self):
		print ("get_weight_thread work")
		while True:
			self.i = int(scale.get_weight(5))
			self.finished.emit(self.i)

# setup scale
scale = HX711(23,24)
scale.set_reference_unit(770)
scale.reset()
scale.tare()
