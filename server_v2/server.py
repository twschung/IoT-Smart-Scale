import os , time, shutil, glob
import ml
import numpy as np
import db_access_server
import obj_recognition

from sklearn import svm
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split


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
    print("IoT Smart Scale Server")
    print("-----------------------------------------------------------")
    print(" [1] - Machine Learning ")
    print(" [2] - Publish System Update ")
    print(" [3] - SQL Database ")
    print(" [4] - Exit ")
    print("-----------------------------------------------------------")
    usrInput=input("Please input the one of the option ->  ")
    if (usrInput == "1"):
        machineLearning_submenu()
    elif (usrInput == "2"):
        publishSystemUpdate_submenu()
    elif (usrInput == "3"):
        SQLdatabase_submenu()
    elif (usrInput == "4"):
        print("Program exiting !!!!")
    else:
        print("Invaild Input")
        wait = input("Press Any Key to continue ... ")
        return main()

def machineLearning_submenu():
    os.system('clear')
    print("Machcine Learning Menu")
    print("-----------------------------------------------------------")
    print(" [1] - Train model")
    print(" [2] - Evaluate model ")
    print(" [3] - Erase training sets and reset ")
    print(" [4] - Back ")
    print("-----------------------------------------------------------")
    usrInput=input("Please input the one of the option ->  ")
    if (usrInput == "1"):
        trainModel()
    elif (usrInput == "2"):
        evaluateModel()
    elif (usrInput == "3"):
        eraseTrainingSetAndReset()
    elif (usrInput == "4"):
        return main()
    else:
        print("Invaild Input")
        wait = input("Press Any Key to continue ... ")
        return machineLearning_submenu()

def publishSystemUpdate_submenu():
    os.system('clear')
    print("Publish System Update Menu")
    print("-----------------------------------------------------------")
    print(" [1] - Publish Trained ML model")
    print(" [2] - Edit Sample Image Version ")
    print(" [3] - Publish local Food DB file")
    print(" [4] - Back ")
    print("-----------------------------------------------------------")
    usrInput = input("Please input the one of the option -> ")
    if (usrInput == "1"):
        publishML()
    elif (usrInput == "2"):
        editImageSampleVersion()
    elif (usrInput == "3"):
        publishLocalFoodDB()
    elif (usrInput == "4"):
        return main()
    else:
        print("Invaild Input")
        wait = input("Press Any Key to continue ... ")
        return publishSystemUpdate_submenu()

def SQLdatabase_submenu():
    os.system('clear')
    print("SQL Database Menu")
    print("-----------------------------------------------------------")
    print(" [1] - Add new Item to Database")
    print(" [2] - Search Item by Category ")
    print(" [3] - Search Item by Descrption ")
    print(" [4] - Back ")
    print("-----------------------------------------------------------")
    usrInput=input("Please input the one of the option ->  ")
    if (usrInput == "1"):
        addNewItemToDB()
    elif (usrInput == "2"):
        searchByCategory()
    elif (usrInput == "3"):
        searchByDescrption()
    elif (usrInput == "4"):
        return main()
    else:
        print("Invaild Input")
        wait = input("Press Any Key to continue ... ")
        return SQLdatabase_submenu()

def trainModel():
    os.system('clear')
    print("-----------------------------------------------------------")
    print("Getting new images from FTP server...")
    totalItemProcessed = 0
    searchPath = os.path.join(exisitingItemPath,'*.jpg')
    for filename in glob.glob(searchPath):
        print("Processing %s ..." % (filename))
        currentPath = filename
        currentBackgroundPath = os.path.join(exisitingItemPath, "backgroundImage" , os.path.basename(filename))
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
    print("Finished modifiing training set. Total of %i items are added"% (totalItemProcessed))
    print("-----------------------------------------------------------")
    print("Moving current ML model to archive")
    try:
        Model_currentPath = os.path.join(os.getcwd(),'Model.dat')
        Model_newFilename = "Model_" + str(os.stat("Model.dat").st_mtime) + ".dat"
        Model_newPath = os.path.join(MLArchivePath, Model_newFilename)
        os.rename(Model_currentPath,Model_newPath)
    except:
        print ("new ML model will be created")
    print("Analysicing which is best ML ...")
    sampleSet = np.load('sampleSet.npy')
    responseSet = np.load('responseSet.npy')
    trainingSS , validationSS , trainingRS , validationRS = train_test_split(sampleSet, responseSet, test_size=0.33, random_state=42)
    clfName = []
    clf = []
    clfscore = []

    clf.append(BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5))
    clfName.append("BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5)")

    # clf.append(svm.LinearSVC())
    # clfName.append("svm.LinearSVC()")

    clf.append(svm.SVC(C=1.0, kernel='linear', probability=True))
    clfName.append("svm.SVC(C=1.0, kernel='linear')")

    clf.append(svm.SVC(C=1.0, kernel='rbf', probability=True))
    clfName.append("svm.SVC(C=1.0, kernel='rbf')")

    clf.append(svm.SVC(C=1.0, kernel='sigmoid', probability=True))
    clfName.append("svm.SVC(C=1.0, kernel='sigmoid')")

    # clf.append(svm.SVC(C=1.0, kernel='poly', degree=3, probability=True))
    # clfName.append("svm.SVC(C=1.0, kernel='poly', degree=3)")

    for x in range (0,len(clf)):
        clf[x].fit(trainingSS,trainingRS)
        clfscore.append(clf[x].score(validationSS,validationRS))
        print (clfName[x]," -> score: ",clfscore[x])
    highestScoredClf = clfscore.index(max(clfscore))
    print("-----------------------------------------------------------")
    print("Traiing will be using ", clfName[highestScoredClf])
    MLmodel = ml.classifier()
    MLmodel.Model = clf[highestScoredClf]
    MLmodel.train()
    print("Finished training ML")
    print("-----------------------------------------------------------")
    wait = input("Press Any Key to continue ... ")
    return machineLearning_submenu()

def evaluateModel():
    os.system('clear')
    print("-----------------------------------------------------------")
    print("Loading Training Set......")
    try:
        sampleSet, responseSet = ml.loadTrainingSet()
        print ("Training set size :")
        print (sampleSet.shape)
        print ("Last modified :")
        fileLastModified = os.stat("sampleSet.npy").st_mtime
        print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(fileLastModified)))
    except:
        print ("No Training Set is found")
        wait = input("Press Any Key to continue ... ")
        return machineLearning_submenu()
    print("Loading ML Info......")
    try:
        print ("Last modified :")
        fileLastModified = os.stat("Model.dat").st_mtime
        print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(fileLastModified)))
    except:
        print ("No ML is found")
        wait = input("Press Any Key to continue ... ")
        return machineLearning_submenu()
    print("-----------------------------------------------------------")
    trainingSS , validationSS , trainingRS , validationRS = train_test_split(sampleSet, responseSet, test_size=0.33, random_state=42)
    clf = ml.classifier()
    clf.load()
    print ("Current machine learning score: ",clf.Model.score(validationSS,validationRS))
    wait = input("Press Any Key to continue ... ")
    return machineLearning_submenu()


def eraseTrainingSetAndReset():
    os.system('clear')
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
    wait = input("Press Any Key to continue ... ")
    return machineLearning_submenu()

def publishML():
    os.system('clear')
    print("Loading ML Info......")
    try:
        print ("Last modified :")
        fileLastModified = os.stat("Model.dat").st_mtime
        print (time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(fileLastModified)))
    except:
        print ("No ML is found")
        wait = input("Press Any Key to continue ... ")
        return publishSystemUpdate_submenu()
    print ("Publishing current classifier model to classifier's path")
    currentPath = os.path.join(os.getcwd(),'Model.dat')
    newPath = os.path.join(MLPath, 'Model.dat')
    shutil.copyfile(currentPath,newPath)
    version = np.array(os.stat("Model.dat").st_mtime)
    np.save('Model_version.npy',version)
    currentPath = os.path.join(os.getcwd(),'Model_version.npy')
    newPath = os.path.join(MLPath, 'Model_version.npy')
    shutil.copyfile(currentPath,newPath)
    print("Complete!")
    print("-----------------------------------------------------------")
    wait = input("Press Any Key to continue ... ")
    return publishSystemUpdate_submenu()

def editImageSampleVersion():
    os.system('clear')
    versionNum =  input("Please enter the new version number for the sample image -> ")
    np.save('imageSample_version.npy',int(versionNum))
    currentPath = os.path.join(os.getcwd(),'imageSample_version.npy')
    newPath = os.path.join(sampleItemPath, 'imageSample_version.npy')
    shutil.copyfile(currentPath,newPath)
    print ("Complete!")
    wait = input("Press Any Key to continue ... ")
    return publishSystemUpdate_submenu()

def publishLocalFoodDB():
    os.system('clear')
    print ("Publishing Local Food Database to Server ...")
    os.system('mysqldump --skip-extended-insert --compact -u terminal_user -pabcd1234 smartscale foodinfo_db > localFoodDB.sql')
    os.system('./mysql2sqlite localFoodDB.sql | sqlite3 localFoodDB.db')
    newFilePath = os.path.join(localDBPath,'localFoodDB.db')
    os.rename('localFoodDB.db',newFilePath)
    print ("Complete!")
    wait = input("Press Any Key to continue ... ")
    return publishSystemUpdate_submenu()

def addNewItemToDB():
    stayInLoop = True
    while (stayInLoop == True):
        os.system('clear')
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
        if (confirmInput.upper == "Y"):
            stayInLoop = False
        elif (confirmInput.upper != "N"):
            print("Invalid Input")
    print("Adding Food item to Database...")
    dbResult = db_access_server.food_register(newFoodInfo)
    if (dbResult[0] == True):
        print("Successfully added to the database :")
        dbResult[1].printFoodDetailsInRow()
    else:
        print("Server Error")
    wait = input("Press Any Key to continue ... ")
    return SQLdatabase_submenu()


def searchByCategory():
    os.system('clear')
    keywordInput=input("Please enter keyword : ")
    dbresult = db_access_server.food_searchByCategory(keywordInput)
    print("Search Result :")
    print("-----------------------------------------------------------")
    if (len(dbresult) > 0):
        for i in range(0,(len(dbresult))):
            foodInfo = db_access_server.foodDataStructure(dbresult[i]['id'],dbresult[i]['category'],dbresult[i]['description'])
            foodInfo.printFoodDetailsInRow()
    print("-----------------------------------------------------------")
    wait = input("Press Any Key to continue ... ")
    return SQLdatabase_submenu()

def searchByDescrption():
    os.system('clear')
    keywordInput=input("Please enter keyword : ")
    dbresult = db_access_server.food_searchByDescription(keywordInput)
    print("Search Result :")
    print("-----------------------------------------------------------")
    if (len(dbresult) > 0):
        for i in range(0,(len(dbresult))):
            foodInfo = db_access_server.foodDataStructure(dbresult[i]['id'],dbresult[i]['category'],dbresult[i]['description'])
            foodInfo.printFoodDetailsInRow()
    print("-----------------------------------------------------------")
    wait = input("Press Any Key to continue ... ")
    return SQLdatabase_submenu()


if __name__ == "__main__":
	main()
