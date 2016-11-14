import ftplib
import urllib.request
import os, time, glob
import numpy as np

FTP_ServerAddress = '42.2.205.124'
FTP_Username = 'admin'
FTP_Password = 'abcd1234'

def connectToServer ():
	session = ftplib.FTP('42.2.205.124','admin','abcd1234')
	return session
	
def generateNewItemFilePath ():
	filename = str(time.time()) + ".jpg"
	filePath = os.path.join(os.getcwd(),"imageHistory/newItem",filename)
	backgroundFilePath = os.path.join(os.getcwd(),"imageHistory/newItem/backgroundImage",filename)
	return filePath , backgroundFilePath

def generateExisitingItemFilePath (imgID):
	filename = str(time.time()) + "_" + str(imgID) + ".jpg"
	filePath = os.path.join(os.getcwd(),"imageHistory/exisitingItem",filename)
	backgroundFilePath = os.path.join(os.getcwd(),"imageHistory/exisitingItem/backgroundImage",filename)
	return filePath , backgroundFilePath
	
def uploadEverythingInFolder(currentFilePath , session)
	searchPath = os.path.join(currentFilePath,'*.jpg')
	for filename in glob.glob(searchPath):
		currentImgPath = os.path.join(currentFilePath,filename)
		imageFile = open(currentImgPath,'rb')
		session.storbinary(('STOR %s'% filename), imageFile)
		imageFile.close()
		os.remove(currentImgPath)
	return session
	
def uploadImageHistory ():
	try:
		session = connectToServer()
		session.cwd ("/imageUploaded/newItem")
		currentFilePath = os.path.join(os.getcwd(),"imageHistory/newItem")
		session = uploadEverythingInFolder(currentFilePath , session)
		session.cwd ("/imageUploaded/newItem/backgroundImage")
		currentFilePath = os.path.join(os.getcwd(),"imageHistory/newItem/backgroundImage")
		session = uploadEverythingInFolder(currentFilePath , session)
		session.cwd ("/imageUploaded/existingItem")
		currentFilePath = os.path.join(os.getcwd(),"imageHistory/existingItem")
		session = uploadEverythingInFolder(currentFilePath , session)
		session.cwd ("/imageUploaded/existingItem/backgroundImage")
		currentFilePath = os.path.join(os.getcwd(),"imageHistory/existingItem/backgroundImage")
		session = uploadEverythingInFolder(currentFilePath , session)
		session.quit()
	except:
		return False
	return True
	
def updateImageSample ():
	try:
		try:
			config = np.load('config.npy').item()
			currentImageSampleVersion = int(config['currentImageSampleVersion'])
		except:
			currentImageSampleVersion = 0
		urllib.request.urlretrieve (('http://42.2.205.124/imageSample/imageSample_version.npy'),'imageSample_version.npy')
		serverImageSampleVersion = np.load('imageSample_version.npy')
		os.remove('imageSample_version.npy')
		if (serverImageSampleVersion > currentImageSampleVersion):
			for nextSampleImage in range((currentImageSampleVersion + 1),(serverImageSampleVersion + 1)):
				nextFilename = str(nextSampleImage) + ".jpg"
				newPath = os.path.join(os.getcwd(),'imageSample',nextFilename)
				try:
					urllib.request.urlretrieve (('http://42.2.205.124/imageSample/%s' % nextFilename),newPath)
				except:
					config['currentImageSampleVersion'] = nextSampleImage
				else:
					config['currentImageSampleVersion'] = nextSampleImage
					np.save('config.npy', config)
	except:
		return (False,0)
	return (True,0)
			
def updateSVM():
	try:
		try:
			config = np.load('config.npy').item()
			currentSVMVersion = float(config['currentSVMVersion'])
		except:
			currentSVMVersion = 0
		urllib.request.urlretrieve (('http://42.2.205.124/SVM/SVM_version.npy'),'SVM_version.npy')
		serverSVMVersion = np.load('SVM_version.npy')
		os.remove('SVM_version.npy')
		if (serverSVMVersion > currentSVMVersion):
			urllib.request.urlretrieve (('http://42.2.205.124/SVM/SVM.dat'),'SVM.dat')
			currentSVMVersion = serverSVMVersion
		config['currentSVMVersion'] = currentSVMVersion
		np.save('config.npy', config)
	except:
		return False
	return True
		
	
def downloadTempImage_3 (filename):
	urllib.request.urlretrieve (('http://42.2.205.124/imageSample/%s' % filename),'temp.jpg')
	


#~ uploadImageHistory ()
#~ updateImageSample()
#~ updateSVM()
