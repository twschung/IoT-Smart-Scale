import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import db_structure, db_access

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
  if (option == "height"):
    if (userInfo.height == ""): errorMsg = "Height can not be blank"
  if (option == "weight"):
    if (userInfo.height == ""): errorMsg = "Weight can not be blank"
  if (errorMsg != ""):
    msg = QMessageBox.information(self, 'Error',errorMsg,QMessageBox.Ok)
    return False
  else: return True
