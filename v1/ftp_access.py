import ftplib
import urllib.request
import os, time
import numpy as np

FTP_ServerAddress = '42.2.205.124'
FTP_Username = 'admin'
FTP_Password = 'abcd1234'

def connectToServer ():
	session = ftplib.FTP('42.2.205.124','admin','abcd1234')
	return session
	
def uploadImage (type, filename, filePath):
	try:
		session = connectToServer()
		session.cwd ("/imageUploaded")
		if (type == "new"):
			session.cwd ("/imageUploaded/newItem")
		elif (type == "exisit"):
			session.cwd ("/imageUploaded/existingItem")
		imageFile = open(filePath,'rb')
		session.storbinary(('STOR %s'% filename), imageFile)
		imageFile.close()
		session.quit()
	except:
		return False
	return True
	
def updateSampleImage ():
	try:
		try:
			config = np.load('config.npy').item()
			lastSampleImageUpdate = int(config['lastSampleImageUpdate'])
		except:
			lastSampleImageUpdate = 0
		stayInLoop = True
		while (stayInLoop == True):
			nextSampleImage = lastSampleImageUpdate + 1
			nextFilename = str(nextSampleImage) + ".jpg"
			try:
				newPath = os.path.join(os.getcwd(),'imageSample',nextFilename)
				urllib.request.urlretrieve (('http://42.2.205.124/imageSample/%s' % nextFilename),newPath)
				lastSampleImageUpdate = nextSampleImage
			except:
				stayInLoop = False
			finally:
				config['lastSampleImageUpdate'] = lastSampleImageUpdate
				np.save('config.npy', config)
	except:
		return False
	return True
			
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
	
#~ updateSampleImage()
#~ updateSVM()
