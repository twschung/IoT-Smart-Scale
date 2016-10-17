import ftplib
import os

def connectToServer ():
	session = ftplib.FTP('42.2.205.124','admin','abcd1234')
	return session
	
def uploadImage (type, filename, filePath):
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
	
def downloadTempImage (filename):
	session = connectToServer()
	session.cwd ("/imageSample")
	session.retrbinary(('RETR %s'% filename), open('temp.jpg','wb').write)
	session.quit()

downloadTempImage("apple.jpg")
	
#uploadImage("exisit", "apple.jpg", "c:/apple.jpg")