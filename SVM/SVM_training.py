import os , time, shutil
import svm
import numpy as np
import imgFeatureExtractSim
import cv2
import db_access


SVMPath = '/home/pi/IoT-Smart-Scale/SVM/FTP/SVM'
SVMArchivePath = '/home/pi/IoT-Smart-Scale/SVM/FTP/SVM/archive'
processedItemPath = '/home/pi/IoT-Smart-Scale/SVM/FTP/imageUploaded/processedItem'
newItemPath = '/home/pi/IoT-Smart-Scale/SVM/FTP/imageUploaded/newItem'
exisitingItemPath =  '/home/pi/IoT-Smart-Scale/SVM/FTP/imageUploaded/existingItem'
sampleItemPath = '/home/pi/IoT-Smart-Scale/SVM/FTP/imageSample'

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
		opt_4()
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
	
def opt_4():
	print("-----------------------------------------------------------")
	print("Fetching new item images!")
	for filename in os.listdir(newItemPath):
		filePath = os.path.join(newItemPath,filename)
		print(filePath)
		previewImage(filePath)
		newImageProcessMenu(filePath)
	main()
	
def newImageProcessMenu(filePath):
	stayInLoop = True
	while (stayInLoop == True):
		print("-----------------------------------------------------------")
		print(" [1] - Assign the current item as new item")
		print(" [2] - Assign the current item as existing item")
		print(" [3] - Look up items from Food_DB ")
		print(" [4] - Preview Image")
		print(" [5] - Skip item")
		print("-----------------------------------------------------------")
		usrInput=input("Please input the one of the option ->  ")
		if (usrInput == "1"):
			inputFood = inputNutritionData()
			print("Adding Food item to Database...")
			dbResult = db_access.food_register(inputFood)
			if (dbResult[0] == True):
				newFilename = os.path.basename(filePath)
				extendion = ("_" + str(dbResult[1].id) + ".jpg")
				newFilename = newFilename.replace(".jpg", extendion)
				newFilePath = os.path.join(exisitingItemPath,newFilename)
				os.rename(filePath,newFilePath)
				currentPath = newFilePath
				newFilename = str(dbResult[1].id) + ".jpg"
				newPath = os.path.join(sampleItemPath, newFilename)
				shutil.copyfile(currentPath,newPath)
				np.save('imageSample_version.npy',dbResult[1].id)
				currentPath = os.path.join(os.getcwd(),'imageSample_version.npy')
				newPath = os.path.join(sampleItemPath, 'imageSample_version.npy')
				shutil.copyfile(currentPath,newPath)
				stayInLoop = False
		elif (usrInput == "2"):
			stayInLoop_2 = True
			while (stayInLoop_2 == True):
				print("-----------------------------------------------------------")
				foodID = input("Please Enter Food Item ID : ")
				foodInfo = db_access.food_getInfo(foodID)
				if (foodInfo[0] == True):
					foodInfo[1].printFoodDetailsInRow()
					confirmInput = input("Confirm ? y/n   ->  ")
					if (confirmInput == "y"):
						stayInLoop_2 = False
						stayInLoop = False
						newFilename = os.path.basename(filePath)
						extendion = ("_" + str(foodID) + ".jpg")
						newFilename = newFilename.replace(".jpg", extendion)
						newFilePath = os.path.join(exisitingItemPath,newFilename)
						os.rename(filePath,newFilePath)
					elif (confirmInput == "n"):
						stayInLoop_2 = True
					else:
						print("Invalid Input")
						stayInLoop_2 = True	
		elif (usrInput == "3"):
			stayInLoop_3 = True
			while (stayInLoop_3 == True):
				print("-----------------------------------------------------------")
				print(" [1] - Search Item by Category")
				print(" [2] - Search Item by Descrption")
				print("-----------------------------------------------------------")
				usrInput=input("Please input the one of the option ->  ")
				if (usrInput == "1"):
					keywordInput=input("Please enter keyword : ")
					dbresult = db_access.food_searchByCategory(keywordInput)
					print("-----------------------------------------------------------")
					if (len(dbresult) > 0):
						for i in range(0,(len(dbresult))):
							foodInfo = db_access.foodDataStructure(dbresult[i]['id'],dbresult[i]['category'],dbresult[i]['description'])
							foodInfo.printFoodDetailsInRow()
					print("-----------------------------------------------------------")
					stayInLoop_3 = False
				elif (usrInput == "2"):
					keywordInput=input("Please enter keyword : ")
					dbresult = db_access.food_searchByDescription(keywordInput)
					print("-----------------------------------------------------------")
					if (len(dbresult) > 0):
						for i in range(0,len(dbresult)):
							foodInfo = db_access.foodDataStructure(dbresult[i]['id'],dbresult[i]['category'],dbresult[i]['description'])
							foodInfo.printFoodDetailsInRow()
					print("-----------------------------------------------------------")
					stayInLoop_3 = False
				else:
					print("Invalid Input")
					stayInLoop_3 = True	
		elif (usrInput == "4"):
			previewImage(filePath)
		elif (usrInput == "5"):
			print("Skipping Item")
			stayInLoop = False
		else:
			print("-----------------------------------------------------------")
			print("ERROR: Invaild Input !!!!!!!")
			print("-----------------------------------------------------------")
		
def previewImage(filePath):
	imgPreview = cv2.imread(filePath)
	cv2.imshow('New Image Preview',imgPreview)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
def inputNutritionData():
	stayInLoop = True
	while (stayInLoop == True):
		newFoodInfo = db_access.foodDataStructure()
		print("-----------------------------------------------------------")
		newFoodInfo.category = input("Please enter category : ")
		newFoodInfo.description = input("Please enter description : ")
		newFoodInfo.fat = input("Please enter fat (g/100g) : ")
		newFoodInfo.saturates = input("Please enter saturates (g/100g) : ")
		newFoodInfo.carbohydrate = input("Please enter carbohydrate (g/100g) : ")
		newFoodInfo.sugars = input("Please enter sugars (g/100g) : ")
		newFoodInfo.fibre = input("Please enter fibre (g/100g) : ")
		newFoodInfo.protein = input("Please enter protein (g/100g) : ")
		newFoodInfo.salt = input("Please enter salt (g/100g) : ")
		print("-----------------------------------------------------------")
		newFoodInfo.printFoodDetails()
		confirmInput = input("Confirm ? y/n   ->  ")
		if (confirmInput == "y"):
			stayInLoop = False
		elif (confirmInput == "n"):
			stayInLoop = True
		else:
			print("Invalid Input")
			stayInLoop = True
	return newFoodInfo

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


if __name__ == "__main__":
	main()
