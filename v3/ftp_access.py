import ftplib
import urllib.request
import os, time, glob
import numpy as np

HTTP_ServerAddress = 'http://151.236.63.243/'
FTP_ServerAddress = '151.236.63.243'
FTP_Username = 'terminal_user'
FTP_Password = 'abcd1234'

def connectToServer ():
	session = ftplib.FTP(FTP_ServerAddress,FTP_Username,FTP_Password)
	return session

def generateNewItemFilePath ():
	filename = str(time.time()) + ".jpg"
	filePath = os.path.join(os.getcwd(),"imageHistory/newItem",filename)
	backgroundFilePath = os.path.join(os.getcwd(),"imageHistory/newItem/backgroundImage",filename)
	return filePath , backgroundFilePath

def generateExisitingItemFilePath (imgID):
	filename = str(time.time()) + "_" + str(imgID) + ".jpg"
	filePath = os.path.join(os.getcwd(),"imageHistory/existingItem",filename)
	backgroundFilePath = os.path.join(os.getcwd(),"imageHistory/existingItem/backgroundImage",filename)
	return filePath , backgroundFilePath

def uploadEverythingInFolder(currentFilePath , session):
	searchPath = os.path.join(currentFilePath,'*.jpg')
	for filePath in glob.glob(searchPath):
		filename = os.path.basename(filePath)
		# currentImgPath = os.path.join(currentFilePath,filename)
		imageFile = open(filePath,'rb')
		session.storbinary(('STOR %s'% filename), imageFile)
		imageFile.close()
		os.remove(filePath)
	return session

def uploadImageHistory ():
	try:
		session = connectToServer()
		session.cwd ("/home/public/FTP/imageUploaded/newItem/")
		currentFilePath = os.path.join(os.getcwd(),"imageHistory/newItem")
		session = uploadEverythingInFolder(currentFilePath , session)
		session.cwd ("/home/public/FTP/imageUploaded/newItem/backgroundImage/")
		currentFilePath = os.path.join(os.getcwd(),"imageHistory/newItem/backgroundImage")
		session = uploadEverythingInFolder(currentFilePath , session)
		session.cwd ("/home/public/FTP/imageUploaded/existingItem/")
		currentFilePath = os.path.join(os.getcwd(),"imageHistory/existingItem")
		session = uploadEverythingInFolder(currentFilePath , session)
		session.cwd ("/home/public/FTP/imageUploaded/existingItem/backgroundImage/")
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
		finally:
			urllib.request.urlretrieve ((HTTP_ServerAddress + '/imageSample/imageSample_version.npy'),'imageSample_version.npy')
			serverImageSampleVersion = np.load('imageSample_version.npy')
			print (serverImageSampleVersion)
			os.remove('imageSample_version.npy')
			if (serverImageSampleVersion > currentImageSampleVersion):
				for nextSampleImage in range((currentImageSampleVersion + 1),(serverImageSampleVersion)):
					nextFilename = str(nextSampleImage) + ".jpg"
					newPath = os.path.join(os.getcwd(),'imageSample',nextFilename)
					urllib.request.urlretrieve ((HTTP_ServerAddress + '/imageSample/%s' % nextFilename),newPath)
				config['currentImageSampleVersion'] = nextSampleImage
				np.save('config.npy', config)
	except:
		return (False,0)
	return (True,0)

def updateML():
	try:
		try:
			config = np.load('config.npy').item()
			try:
				currentMLVersion = float(config['currentMLVersion'])
			except:
				currentMLVersion = 0
		except:
			currentMLVersion = 0
		urllib.request.urlretrieve ((HTTP_ServerAddress + '/ML/Model_version.npy'),'Model_version.npy')
		serverMLVersion = np.load('Model_version.npy')
		os.remove('Model_version.npy')
		if (serverMLVersion > currentMLVersion):
			# urllib.request.urlretrieve ((HTTP_ServerAddress + '/ML/ML.dat'),'ML.dat')
			# urllib.request.urlretrieve ((HTTP_ServerAddress + '/ML/PCA.dat'),'PCA.dat')
			urllib.request.urlretrieve ((HTTP_ServerAddress + '/ML/Model.dat'),'Model.dat')
			# urllib.request.urlretrieve ((HTTP_ServerAddress + '/ML/Tree.npy'),'Tree.npy')
			currentMLVersion = serverMLVersion
		config['currentMLVersion'] = currentMLVersion
		np.save('config.npy', config)
	except:
		return False
	return True

def updatelocalDB():
	try:
		urllib.request.urlretrieve ((HTTP_ServerAddress + '/DB/localFoodDB.db'),'localFoodDB.db')
	except:
		return False
	return True


# updateML()
#~ uploadImageHistory ()
#~ updateImageSample()
#~ updateML()
