import os , time, shutil, glob
import svm
import numpy as np
import db_access, ftp_access
import obj_recognition

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

def main():
	print("IoT Smart Scale Terminal-End Testing & Training Program")
	print("-----------------------------------------------------------")
	print(" [1] - Start Camera Preview ")
	print(" [2] - Take Pictures for Sample Set")
	print(" [3] - Upload Sample Set Images to FTP Server ")
	print(" [4] - Fetch New Trained Model from Server ")
	print(" [5] - Test out Trained Model ")
	print(" [6] - Exit Program ")
	print("-----------------------------------------------------------")
	usrInput=input("Please input the one of the option ->  ")
	if (usrInput == "1"):
		opt_1()
	elif (usrInput == "2"):
		opt_2()
	elif (usrInput == "3"):
		opt_3()
	elif (usrInput == "4"):
		opt_4()
	elif (usrInput == "5"):
		opt_5()
	elif (usrInput == "6"):
		print("Program exiting !!!!")
	else:
		print("-----------------------------------------------------------")
		print("ERROR: Invaild Input !!!!!!!")
		print("-----------------------------------------------------------")
		main()

def opt_1():
	print("-----------------------------------------------------------")
	print("Starting Camera Preview...")
	camera.start_preview()
	GPIO.output(12,True)
	input("Press any button to exit")
	camera.stop_preview()
	GPIO.output(12,False)
	print("-----------------------------------------------------------")
	main()

def opt_2():
	print("-----------------------------------------------------------")
	foodID = input("Please Enter Food ID Number")
	numOfSample = int(input("Please Enter the Number of samples you wish to take"))
	while (numOfSample > 0):
		forgroundFilePath, backgroundFilePath = ftp_access.generateExisitingItemFilePath(foodID)
		print("Sample : " + str(numOfSample))
		input("Tell me when Background is Ready")
		GPIO.output(12,True)
		camera.start_preview()
		sleep(2)
		camera.capture(backgroundFilePath)
		camera.stop_preview()
		GPIO.output(12,False)
		input("Tell me when Forground is Ready")
		GPIO.output(12,True)
		camera.start_preview()
		sleep(2)
		camera.capture(forgroundFilePath)
		camera.stop_preview()
		GPIO.output(12,False)
		numOfSample -= 1
	print("-----------------------------------------------------------")
	main()

def opt_3():
	print("-----------------------------------------------------------")
	print("Uploading Image to Server!")
	ftp_access.uploadImageHistory()
	print("Done!")
	print("-----------------------------------------------------------")
	main()

def opt_4():
	print("-----------------------------------------------------------")
	print("Fetching Trained Model from Server!")
	ftp_access.updateSVM()
	print("Done!")
	displaySVMInfo()
	print("-----------------------------------------------------------")
	main()

def opt_5():
	print("-----------------------------------------------------------")
	input("Tell me when Background is Ready")
	GPIO.output(12,True)
	camera.start_preview()
	sleep(2)
	camera.capture("background.jpg")
	camera.stop_preview()
	GPIO.output(12,False)
	input("Tell me when Forground is Ready")
	GPIO.output(12,True)
	camera.start_preview()
	sleep(2)
	camera.capture("forground.jpg")
	camera.stop_preview()
	GPIO.output(12,False)
	imageFeature = obj_recognition.main("forground.jpg", "background.jpg")
	print("-----------------------------------------------------------")
	clf = SVM()
	clf.load()
	clfResult = clf.predict(imageFeature)
	foodInfo = db_access.food_getInfo(clfResult)
	foodInfo.printFoodDetailsInRow()
	print(clf.predict_prob(imageFeature))
	print("-----------------------------------------------------------")
	main()


def displaySVMInfo():
	print("Loading SVM Info......")
	try:
		print ("Last modified :")
		fileLastModified = os.stat("SVM.dat").st_mtime
		print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(fileLastModified)))
	except:
		print ("No SVM is found")


if __name__ == "__main__":
	main()
