import ftplib
import urllib.request
import os, time

FTP_ServerAddress = '42.2.205.124'
FTP_Username = 'admin'
FTP_Password = 'abcd1234'

def connectToServer ():
	session = ftplib.FTP('42.2.205.124','admin','abcd1234')
	return session
	
def disconnectFromServer (session):
	session.quit()
	
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
	
def downloadTempImage_1 (session, filename):
	session.cwd ("/imageSample")
	session.retrbinary(('RETR %s'% filename), open('temp.jpg','wb').write)
	
def downloadTempImage_2 (filename):
	session = connectToServer()
	session.cwd ("/imageSample")
	session.retrbinary(('RETR %s'% filename), open('temp.jpg','wb').write)
	session.quit()
	
def downloadTempImage_3 (filename):
	urllib.request.urlretrieve (('http://42.2.205.124/imageSample/%s' % filename),'temp.jpg')
	


#downloadTempImage("apple.jpg")
# tic = time.clock()
# uploadImage("exisit", "apple.jpg", "c:/apple.jpg")
# toc = time.clock()
# print((toc - tic))