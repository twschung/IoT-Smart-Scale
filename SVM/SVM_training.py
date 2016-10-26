import os , time, shutil
import svm
import numpy as np
import imgFeatureExtractSim

SVMPath = '/home/pi/Desktop/IoT-Smart-Scale/v1/SVM/FTP/SVM'
SVMArchivePath = '/home/pi/Desktop/IoT-Smart-Scale/v1/SVM/FTP/SVM/archive'
processedItemPath = '/home/pi/Desktop/IoT-Smart-Scale/v1/SVM/FTP/imageUploaded/processedItem'
newItemPath = '/home/pi/Desktop/IoT-Smart-Scale/v1/SVM/FTP/imageUploaded/newItem'
exisitingItemPath =  '/home/pi/Desktop/IoT-Smart-Scale/v1/SVM/FTP/imageUploaded/exisitingItem/'

def main():
	print("IoT Smart Scale SVM Training Program")
	print("-----------------------------------------------------------")
	print(" [1] - Current Training sets and Trained SVM model's info ")
	print(" [2] - Fetch new data from queue and add to the current training sets & Train SVM ")
	print(" [3] - Publish the trained SVM ")
	print(" [4] - Add new item into database & add into the data training queue ")
	print(" [5] - Exit Program ")
	print("-----------------------------------------------------------")
	usrInput=input("Please input the one of the option ->  ")
	if (usrInput == "1"):
		opt_1()
	elif (usrInput == "2"):
		opt_2()
	elif (usrInput == "3"):
		opt_3()
	elif (usrInput == "4"):
		path = "/home/pi/Desktop/IoT-Smart-Scale/v1/SVM/FTP/imageUploaded/exisitingItem/1474676686.9362292_1.jpg"
		print(imgFeatureExtractSim.sim(path))
	elif (usrInput == "5"):
		print("Program exiting !!!!")
	else:
		print("-----------------------------------------------------------")
		print("ERROR: Invaild Input !!!!!!!")
		print("-----------------------------------------------------------")
		main()

def opt_1():
	displayTrainingDataInfo()
	displaySVMInfo()
	main()

def opt_2():
	print("-----------------------------------------------------------")
	print("Getting images from queue...")
	totalItemProcessed = 0
	for filename in os.listdir(exisitingItemPath):
		print("Processing %s ..." % (filename))
		currentPath = os.path.join(exisitingItemPath,filename)
		imgFeature = imgFeatureExtractSim.sim(currentPath)
		time, imgID = filename.split("_")
		imgID, fileExtendion = imgID.split(".")
		svm.addNewDataSet(imgFeature,int(imgID))
		newPath = os.path.join(processedItemPath,filename)
		os.rename(currentPath,newPath)
		totalItemProcessed = totalItemProcessed + 1
	print("Finished modifiing training set. Total of %i is added"% (totalItemProcessed))
	if (totalItemProcessed > 0):
		displayTrainingDataInfo()
		print("Moving current SVM model to archive")
		currentPath = os.path.join(os.getcwd(),'SVM.dat')
		newFilename = "SVM_" + str(os.stat("SVM.dat").st_mtime) + ".dat"
		newPath = os.path.join(SVMArchivePath, newFilename)
		os.rename(currentPath,newPath)
		print("Training SVM from Training Set...")
		SVMmodel = svm.SVM()
		SVMmodel.train()
		print("Finished training SVM")
		displaySVMInfo()
	else:
		print("SVM Training is skipped, as no new image is processed")
	print("-----------------------------------------------------------")
	main()

def opt_3():
	displaySVMInfo()
	print ("Publishing current SVM model to SVM path")
	currentPath = os.path.join(os.getcwd(),'SVM.dat')
	newPath = os.path.join(SVMPath, 'SVM.dat')
	shutil.copyfile(currentPath,newPath)
	version = np.array(os.stat("SVM.dat").st_mtime)
	np.save('SVM_version.npy',version)
	currentPath = os.path.join(os.getcwd(),'SVM_version.npy')
	newPath = os.path.join(SVMPath, 'SVM_version.npy')
	shutil.copyfile(currentPath,newPath)
	print("Done!")
	print("-----------------------------------------------------------")
	main()
	
def displayTrainingDataInfo():
	print("-----------------------------------------------------------")
	print("Loading Training Set......")
	try:
		sampleSet, responseSet = svm.loadTrainingSet()
		print ("Training set size :")
		print (sampleSet.shape)
		print ("Last modified :")
		fileLastModified = os.stat("sampleSet.npy").st_mtime
		print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(fileLastModified)))
	except:
		print ("No Training Set is found")
	print("-----------------------------------------------------------")

def displaySVMInfo():
	print("Loading SVM Info......")
	try:
		print ("Last modified :")
		fileLastModified = os.stat("SVM.dat").st_mtime
		print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(fileLastModified)))
	except:
		print ("No SVM is found")
	#~ try:
		#~ lastestSVMInfo = np.load('config.npy').item()
		#~ print ("SVM model created date :")
		#~ print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(lastestSVMInfo[dateCreated])))
		#~ print ("Training set size :")
		#~ print (lastestSVMInfo[sampleSetSize])
		#~ print ("Training set last modified :")
		#~ print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(lastestSVMInfo[sampleSetLastModified])))
	#~ except:
		#~ print ("No SVM model found")

if __name__ == "__main__":
	main()
