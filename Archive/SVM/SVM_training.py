import os , time, shutil, glob
import ml
import numpy as np
import imgFeatureExtractSim
import db_access_server
import obj_recognition
import evaluateML


MLPath = '/home/public/HTTP/ML'
MLArchivePath = '/home/public/HTTP/ML/archive'
processedItemPath = '/home/public/FTP/imageUploaded/processedItem'
newItemPath = '/home/public/FTP/imageUploaded/newItem'
exisitingItemPath =  '/home/public/FTP/imageUploaded/existingItem'
exisitingBackgroundItemPath = '/home/public/FTP/imageUploaded/existingItem/backgroundImage'
sampleItemPath = '/home/public/HTTP/imageSample'
localDBPath = '/home/public/HTTP/DB'

def main():
	os.system('clear')
	print("IoT Smart Scale ML Training Program")
	print("-----------------------------------------------------------")
	print(" [1] - Current Training sets and Trained ML model's info ")
	print(" [2] - Fetch new data from queue and add to the current training sets & Train ML ")
	print(" [3] - Publish the trained ML ")
	print(" [4] - Add new item into database & add into the data training queue ")
	print(" [5] - Exit Program ")
	print(" [6] - Erase SampleSet & RasposeSet and reset everything")
	print(" [7] - Editing sampleImageVersion.npy")
	print(" [8] - Evaluate Machine Learning")
	print(" [9] - Export and Publish Food DB into sqlite format")
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
	elif (usrInput == "6"):
		opt_6()
	elif (usrInput == "7"):
		opt_7()
	elif (usrInput == "8"):
		opt_8()
	elif (usrInput == "9"):
		opt_9()

def opt_1():
	displayTrainingDataInfo()
	displayMLInfo()
	wait = input("Press Any Key to continue ... ")
	main()

def opt_2():
	print("-----------------------------------------------------------")
	print("Getting images from queue...")
	totalItemProcessed = 0
	searchPath = os.path.join(exisitingItemPath,'*.jpg')
	for filename in glob.glob(searchPath):
		print("Processing %s ..." % (filename))
		currentPath = filename
		currentBackgroundPath = os.path.join(exisitingItemPath, "backgroundImage" , os.path.basename(filename))
		#~ imgFeature = imgFeatureExtractSim.sim(currentPath) ###
		imgFeature = obj_recognition.main(currentPath,currentBackgroundPath)
		imgFeature = np.nan_to_num(imgFeature)
		time, imgID = os.path.basename(filename).split("_")
		imgID, fileExtendion = imgID.split(".")
		ml.addNewDataSet(imgFeature,int(imgID))
		newPath = os.path.join(processedItemPath,os.path.basename(filename))
		newBackgroundPath = os.path.join(processedItemPath, 'backgroundImage', os.path.basename(filename))
		os.rename(currentPath,newPath)
		os.rename(currentBackgroundPath,newBackgroundPath)
		totalItemProcessed = totalItemProcessed + 1
	print("Finished modifiing training set. Total of %i is added"% (totalItemProcessed))
	if (totalItemProcessed > -1):
		displayTrainingDataInfo()
		print("Moving current ML model to archive")
		try:
			# svm_currentPath = os.path.join(os.getcwd(),'ML.dat')
			# svm_newFilename = "ML_" + str(os.stat("ML.dat").st_mtime) + ".dat"
			# svm_newPath = os.path.join(MLArchivePath, svm_newFilename)
			# pca_currentPath = os.path.join(os.getcwd(),'PCA.dat')
			# pca_newFilename = "PCA_" + str(os.stat("ML.dat").st_mtime) + ".dat"
			# pca_newPath = os.path.join(MLArchivePath, pca_newFilename)
			Model_currentPath = os.path.join(os.getcwd(),'Model.dat')
			Model_newFilename = "Model_" + str(os.stat("Model.dat").st_mtime) + ".dat"
			Model_newPath = os.path.join(MLArchivePath, Model_newFilename)
			os.rename(Model_currentPath,Model_newPath)
		except:
			print ("new ML model will be created")
		finally:
			print("Training ML from Training Set...")
			MLmodel = ml.classifier()
			MLmodel.train()
			print("Finished training ML")
			displayMLInfo()
	else:
		print("ML Training is skipped, as no new image is processed")
	print("-----------------------------------------------------------")
	wait = input("Press Any Key to continue ... ")
	main()

def opt_3():
	displayMLInfo()
	print ("Publishing current classifier model to classifier's path")
	# currentPath = os.path.join(os.getcwd(),'ML.dat')
	# newPath = os.path.join(MLPath, 'ML.dat')
	# shutil.copyfile(currentPath,newPath)
	# currentPath = os.path.join(os.getcwd(),'PCA.dat')
	# newPath = os.path.join(MLPath, 'PCA.dat')
	# shutil.copyfile(currentPath,newPath)
	currentPath = os.path.join(os.getcwd(),'Model.dat')
	newPath = os.path.join(MLPath, 'Model.dat')
	shutil.copyfile(currentPath,newPath)
	version = np.array(os.stat("Model.dat").st_mtime)
	np.save('Model_version.npy',version)
	currentPath = os.path.join(os.getcwd(),'Model_version.npy')
	newPath = os.path.join(MLPath, 'Model_version.npy')
	shutil.copyfile(currentPath,newPath)
	print("Done!")
	print("-----------------------------------------------------------")
	wait = input("Press Any Key to continue ... ")
	main()

def opt_4():
	print("-----------------------------------------------------------")
	print("Fetching new item images!")
	searchPath = os.path.join(newItemPath,'*.jpg')
	for filename in glob.glob(searchPath):
		filePath = os.path.join(newItemPath,filename)
		print(filePath)
		previewImage(filePath)
		newImageProcessMenu(filePath)
	wait = input("Press Any Key to continue ... ")
	main()

def opt_6():
	print("-----------------------------------------------------------")
	print("Moving images from processedItem's folder to existingItem's folder !")
	searchPath = os.path.join(processedItemPath,'*.jpg')
	for filename in glob.glob(searchPath):
		currentFilePath = filename
		newFilePath = os.path.join(exisitingItemPath, (os.path.basename(filename)))
		print("Moving ",currentFilePath , " to ", newFilePath)
		os.rename(currentFilePath,newFilePath)
	searchPath = os.path.join(processedItemPath,'backgroundImage/*.jpg')
	for filename in glob.glob(searchPath):
		currentFilePath = filename
		newFilePath = os.path.join(exisitingBackgroundItemPath,(os.path.basename(filename)))
		print("Moving ",currentFilePath , " to ", newFilePath)
		os.rename(currentFilePath,newFilePath)
	try:
		print ("Removing sampleSet and responseSet")
		os.remove("sampleSet.npy")
		os.remove("responseSet.npy")
	except:
		print ("No sampleSet or responseSet is found")
	finally:
		wait = input("Press Any Key to continue ... ")
		main()

def opt_7():
	versionNum =  input("Please enter the new version number for the sample image -> ")
	np.save('imageSample_version.npy',versionNum)
	currentPath = os.path.join(os.getcwd(),'imageSample_version.npy')
	newPath = os.path.join(sampleItemPath, 'imageSample_version.npy')
	shutil.copyfile(currentPath,newPath)
	print ("Finish editing sampleImageVersion.npy")
	wait = input("Press Any Key to continue ... ")
	main()

def opt_8():
	evaluateML.evaluateML()
	wait = input("Press Any Key to continue ... ")
	main()

def opt_9():
	os.system('mysqldump --skip-extended-insert --compact -u terminal_user -pabcd1234 smartscale foodinfo_db > localFoodDB.sql')
	os.system('./mysql2sqlite localFoodDB.sql | sqlite3 localFoodDB.db')
	newFilePath = os.path.join(localDBPath,'localFoodDB.db')
	os.rename('localFoodDB.db',newFilePath)
	main()

def newImageProcessMenu(filePath):
	stayInLoop = True
	while (stayInLoop == True):
		os.system('clear')
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
			dbResult = db_access_server.food_register(inputFood)
			if (dbResult[0] == True):
				newFilename = os.path.basename(filePath)
				extendion = ("_" + str(dbResult[1].id) + ".jpg")
				newFilename = newFilename.replace(".jpg", extendion)
				newFilePath = os.path.join(exisitingItemPath,newFilename)
				os.rename(filePath,newFilePath)
				backgroundImgPath = os.path.join(newItemPath,'backgroundImage', (os.path.basename(filePath)))
				newBackgroundImgPath = os.path.join(exisitingItemPath,'backgroundImage',newFilename)
				os.rename(backgroundImgPath, newBackgroundImgPath)

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
				foodInfo = db_access_server.food_getInfo(foodID)
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
						backgroundImgPath = os.path.join(newItemPath,'backgroundImage', (os.path.basename(filePath)))
						newBackgroundImgPath = os.path.join(exisitingItemPath,'backgroundImage',newFilename)
						os.rename(backgroundImgPath, newBackgroundImgPath)
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
					dbresult = db_access_server.food_searchByCategory(keywordInput)
					print("-----------------------------------------------------------")
					if (len(dbresult) > 0):
						for i in range(0,(len(dbresult))):
							foodInfo = db_access_server.foodDataStructure(dbresult[i]['id'],dbresult[i]['category'],dbresult[i]['description'])
							foodInfo.printFoodDetailsInRow()
					print("-----------------------------------------------------------")
					stayInLoop_3 = False
				elif (usrInput == "2"):
					keywordInput=input("Please enter keyword : ")
					dbresult = db_access_server.food_searchByDescription(keywordInput)
					print("-----------------------------------------------------------")
					if (len(dbresult) > 0):
						for i in range(0,len(dbresult)):
							foodInfo = db_access_server.foodDataStructure(dbresult[i]['id'],dbresult[i]['category'],dbresult[i]['description'])
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
		newFoodInfo = db_access_server.foodDataStructure()
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

def displayMLInfo():
	print("Loading ML Info......")
	try:
		print ("Last modified :")
		fileLastModified = os.stat("Model.dat").st_mtime
		print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(fileLastModified)))
	except:
		print ("No ML is found")


if __name__ == "__main__":
	main()
