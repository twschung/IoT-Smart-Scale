#import matplotlib.pyplot as plt
from multiprocessing import Process, Queue
import os
import sys
import numpy as np
import cv2
import cv2.xfeatures2d
import mahotas
import mahotas.features

def main(imgPath,bgPath):
	img = cv2.imread(imgPath)
	background = cv2.imread(bgPath)
	#obj, mask, cnt = backgroundSubtraction2(img)
	queue = Queue()
	queue2 = Queue()
	# queue3 = Queue()
	# queue4 = Queue()
	imgP = Process(target=resizeImg, args=(img,queue))
	bgP = Process(target=resizeImg, args=(background,queue2))
	imgP.start()
	bgP.start()
	img = queue.get()
	background = queue2.get()
	imgP.join()
	bgP.join()
	try:
		obj, mask, cnt = backgroundSubtraction(img,background)
		col = Process(target=colourHist(obj,mask,queue))
		text = Process(target=haralick, args=(obj,queue2))
		# orb = Process(target=orbDetect, args=(obj.copy(),queue3))
		# kaze = Process(target=orbDetect, args=(obj.copy(),queue4))
		col.start()
		text.start()
		# orb.start()
		# kaze.start()
		colour_set = queue.get()
		texture = queue2.get()
		# ORBdes = queue3.get()
		# KAZEdes = queue4.get()
		col.join()
		text.join()
		# orb.join()
		# kaze.join()
		H, area, perimeter, diameter = shapes(img,cnt)
		# if(ORBdes[0] == None):
		# 	ORBdes = np.zeros((6000,),dtype=np.int)
		# else:
		# 	ORBdes = np.pad(ORBdes,(0,6000-ORBdes.size),'constant',constant_values=0)
		# if(KAZEdes[0] == None):
		# 	KAZEdes = np.zeros((10000,),dtype=np.int)
		# else:
		# 	KAZEdes = np.pad(KAZEdes,(0,10000-KAZEdes.size),'constant',constant_values=0)
		ORBdes=0
		KAZEdes=0
		obj_array = appendAll(colour_set,H,area,perimeter,diameter,texture,ORBdes,KAZEdes)
		obj_array = np.float64(obj_array)
		#print(obj_array.shape)
		resultValid = True
	except:
		print('Error: Unable to detect food item')
		obj_array = np.nan * np.empty(71)
		#print(obj_array.shape)
		resultValid = False
	
	return obj_array, resultValid

def denoise(img):
	# This method uses non-local mean to denoise the image
	denoised = cv2.fastNlMeansDenoisingColored(img,None,8,10,7,21)
	return denoised

def resizeImg(img,queue):
	# This method simply resizes the image
	img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
	queue.put(img)

def displayImg(title,img):
	# This method simply displays the image to the user
	cv2.imshow(title,img)
	cv2.waitKey(0)

def cropImg(img, mask, cnt):
	# This method crops out the black areas of the image
	# This method with called within 'findObjectCanny'
	x,y,w,h = cv2.boundingRect(cnt)
	cropped = img[y:y+h,x:x+w]
	mask = mask[y:y+h,x:x+w]
	return cropped, mask

def backgroundSubtraction(img, background):
	# This method extracts the foreground item from the background
	fgbg = cv2.createBackgroundSubtractorMOG2(1, 355, False) # manual threshold
	fgmask = fgbg.apply(background)
	fgmask = fgbg.apply(img)
	subtracted = cv2.bitwise_and(img,img,mask = fgmask)
	subtracted, fgmask, cnt = findCnt(subtracted, fgmask)
	#displayImg('subtracted',subtracted)
	return subtracted, fgmask, cnt
	
def backgroundSubtraction2(img):
	img = cv2.bilateralFilter(img, 12, 8, 8)
	lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
	l,a,b = cv2.split(lab)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(12,12))
	cl = clahe.apply(l)
	limg = cv2.merge((cl,a,b))
	img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#hsv_img[:,:,1] = cv2.bilateralFilter(hsv_img[:,:,1], 20, 8, 8)
	hsv_img[:,:,1]= cv2.GaussianBlur(hsv_img[:,:,1],(5,5),0)
	_,hsv_img[:,:,1] = cv2.threshold(hsv_img[:,:,1],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	kernel = np.ones((10,10),np.uint8)
	hsv_img[:,:,1] = cv2.morphologyEx(hsv_img[:,:,1], cv2.MORPH_OPEN, kernel)
	#cv2.imshow("hsv", hsv_img[:,:,1])
	edged = cv2.Canny(hsv_img[:,:,1],50,200)
	#cv2.imshow('edges',edged)
	
	_,contours,_ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key = cv2.contourArea, reverse=True)
	mask = np.zeros(img.shape, np.uint8)
		
	for c in contours:
		if cv2.contourArea(c)<678000 and cv2.contourArea(c)>10:
			print(cv2.contourArea(c)) #678756
			hull = cv2.convexHull(c)
			cv2.drawContours(img, [hull], -1, (0, 0, 255), 1)		
			cv2.drawContours(mask, [hull], -1, (255,255,255), -1)
			break
	cv2.imshow("Show",img)
	#img, mask = cropImg(img, mask, hull)
	#cv2.imshow("Mask",mask)
	cv2.waitKey()
	
	return img, mask, hull

def findCnt(img, mask):
	# This method finds the contour and crops the image as well
	_,contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key = cv2.contourArea, reverse = True)
	cnt = contours[0]
	img, mask = cropImg(img, mask, cnt)
	# displayImg('cropped',img)
	return img, mask, cnt

def colourHist(img, mask,queue):
	color = ('b','g','r')
	norm_set = []
	for channel,col in enumerate(color):
		hist = cv2.calcHist([img],[channel],mask,[16],[0,256])
		norm = cv2.normalize(hist, hist, 1, 0, cv2.NORM_L1, -1)
		norm_set.append(norm)
		'''
		plt.plot(norm,color = col)
		plt.xlim([0,16])
	plt.title('Normalized histogram for color scale picture')
	plt.show()
	print("Colour Histogram", norm_set)
	'''
	queue.put(norm_set)

def shapes(img,cnt):
	# this method computes all sorts of shape descriptors
	H = cv2.HuMoments(cv2.moments(cnt)).flatten()
	area = cv2.contourArea(cnt)
	area = area/61088
	perimeter = cv2.arcLength(cnt,True)
	(x,y),radius = cv2.minEnclosingCircle(cnt)
	diameter = radius*2
	return H, area, perimeter, diameter

def haralick(img,queue):
	# this method computes the Haralick texture features
	texture = mahotas.features.haralick(img).mean(0)
	queue.put(texture)

def orbDetect(img,queue):
	# Initiate STAR detector
	orb = cv2.ORB_create()
	# find the keypoints with ORB
	kp = orb.detect(img,None)
	# compute the descriptors with ORB
	kp, des = orb.compute(img, kp)
	des = np.ravel(np.array(des))
	queue.put(des)

def kazeDetect(img,queue):
	# load the image and convert it to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # initialize the KAZE descriptor, then detect keypoints and extract local invariant descriptors from the image
    detector = cv2.KAZE_create()
    kp, des = detector.detectAndCompute(gray, None)
    des = np.ravel(np.array(des))
    queue.put(des)

def appendAll(colour_set,H,area,perimeter,diameter,texture,ORBdes, KAZEdes):
	obj_array = np.ravel(np.array(colour_set))
	obj_array = np.append(obj_array,H)
	obj_array = np.append(obj_array,area)
	obj_array = np.append(obj_array,perimeter)
	obj_array = np.append(obj_array, diameter)
	obj_array = np.append(obj_array,texture)
	# obj_array = np.append(obj_array,ORBdes)
	# obj_array = np.append(obj_array,KAZEdes)
	return obj_array