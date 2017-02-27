import sys
import os
currentDir = os.getcwd()
sys.path.insert(0,currentDir+"/src")
sys.path.insert(0,currentDir+"/ui")
import datetime
from decimal import Decimal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import db_structure, db_access
i = datetime.datetime.now()

def checkUserDetails(self,userInfo, option):
  errorMsg = ""
  if (option == "email"):
    if (userInfo.email == ""): errorMsg = "Email can not be blank"
    elif (" " in userInfo.email ): errorMsg = "Email can not contain Space"
    elif ("@" not in userInfo.email ): errorMsg = "Invaild email format"
    elif (db_access.user_checkIfEmailAlreadyRegisted(userInfo.email) == True): errorMsg = "This email address is already regsistered"
  if (option == "firstname"):
    if (userInfo.firstname == ""): errorMsg = "First name can not be blank"
  if (option == "lastname"):
    if (userInfo.lastname == ""): errorMsg = "Last name can not be blank"
  if (option == "dob"):
    if (userInfo.dob == ""): errorMsg = "Year of Birth can not be blank"
    elif (len(userInfo.dob)>4): errorMsg = "Year of Birth can not be longer than 4 digits"
    elif (int(userInfo.dob)<1875 or int(userInfo.dob)>i.year): errorMsg = "Year of Birth entered is unrealistic"
  if (option == "height"):
    if (userInfo.height == ""): errorMsg = "Height can not be blank"
    elif (Decimal(userInfo.height)>3 or Decimal(userInfo.height)<0.5): errorMsg = "Height entered is unrealistic"
  if (option == "weight"):
    if (userInfo.weight == ""): errorMsg = "Weight can not be blank"
    elif (Decimal(userInfo.weight)>300 or Decimal(userInfo.weight)<2): errorMsg = "Weight entered is unrealistic"
  if (option == "targetWeight"):
    if (userInfo.targetWeight == ""): errorMsg = "Target weight can not be blank"
    elif (Decimal(userInfo.targetWeight)>300 or Decimal(userInfo.targetWeight)<2): errorMsg = "Target weight entered is unrealistic"
  if (option == "targetIntake"):
    if (userInfo.targetIntake == ""): errorMsg = "Target intake can not be blank"
  if (errorMsg != ""):
    msg = QMessageBox.information(self, 'Error',errorMsg,QMessageBox.Ok)
    return False
  else: return True
