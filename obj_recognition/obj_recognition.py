from matplotlib import pyplot as plt
import os
import sys
import numpy as np
import cv2
import cv2.xfeatures2d
import mahotas
import mahotas.features

def main(imgPath,bgPath):
	img = cv2.imread(imgPath)
	if(os.path.exists(imgPath) == False):
		print("Foreground image path doesn't exists. Try again.")
	background = cv2.imread(bgPath)
	if(os.path.exists(bgPath) == False):
		print("Background image path doesn't exists. Try again.")
	img = resizeImg(img)
	background = resizeImg(background)
	img = denoise(img)
	background = denoise(background)
	subtracted = backgroundSubtraction(img,background)
	obj, mask, cnt = findObjectCanny(subtracted)
	colour_set = colourHist(obj, mask)
	H, area, perimeter, approx, hull, convexity, ellipse = shapes(cnt)
	texture = haralick(obj)
	ORBdes = orbDetect(obj.copy())
	SURFdes, FREAKdes = freakDetect(obj.copy())
	obj_array = appendAll(colour_set,H,area,perimeter,approx,hull,convexity,ellipse,texture,ORBdes,SURFdes,FREAKdes)
	#print(obj_array.shape)
	cv2.destroyAllWindows
	return obj_array

def denoise(img):
	# This method uses non-local mean to denoise the image
	denoised = cv2.fastNlMeansDenoisingColored(img,None,8,10,7,21)
	return denoised

def resizeImg(img):
	# This method simply resizes the image
	img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
	return img
	
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
	#displayImg('fgmask', fgmask)
	blurbg = cv2.GaussianBlur(img,(15,15),0)
	#displayImg('blurmask',blurbg)
	invmask = cv2.bitwise_not(fgmask)
	blurbg = cv2.bitwise_and(blurbg,blurbg,mask = invmask)
	subtracted = cv2.bitwise_and(img,img,mask = fgmask)
	subtracted = cv2.bitwise_or(subtracted,blurbg)
	#displayImg('subtracted',subtracted)
	return subtracted

def findObjectCanny(img):
	# This method implements the Canny Edge Detector
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#displayImg('gray',gray)
	#blurred = cv2.medianBlur(gray,5)
	#displayImg('blurred',blurred)
	th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) # manual threshold
	#displayImg('th',th)
	kernel = np.ones((5,5),np.uint8)
	opened = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
	#displayImg('opened',opened)
	edged = cv2.Canny(opened, 15, 255) # manual threshold
	#displayImg('edged',edged)
	edged = cv2.bitwise_not(edged);
	edged = cv2.morphologyEx(edged, cv2.MORPH_OPEN, kernel)
	#displayImg('edged-opened',edged)
	edged = cv2.bitwise_not(opened)
	_,contours,_ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key = cv2.contourArea, reverse = True)
	cnt = contours[0]
	mask = np.zeros(gray.shape, dtype=np.uint8)
	cv2.drawContours(mask, [cnt], -1, (255, 0, 0), -1)
	#displayImg('contoured',mask)
	obj = cv2.bitwise_and(img,img,mask = mask)
	#displayImg('object',obj)
	obj, mask = cropImg(obj, mask, cnt)
	displayImg('cropped',obj)
	return obj, mask, cnt

def colourHist(img, mask):
	color = ('b','g','r')
	norm_set = []
	for channel,col in enumerate(color):
		hist = cv2.calcHist([img],[channel],mask,[32],[0,32])
		norm = cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX,-1)
		norm_set.append(norm);
		#plt.plot(norm,color = col)
		#plt.xlim([0,32])
	#plt.title('Normalized histogram for color scale picture')
	#plt.show()
	norm_set = np.array(norm_set)
	np.reshape(norm_set, -1, 3)
	#print("Colour Histogram", norm_set)
	return norm_set

def shapes(cnt):
	# this method computes all sorts of shape descriptors
	H = cv2.HuMoments(cv2.moments(cnt)).flatten()
	#print("Hu Moments: ",H)
	area = cv2.contourArea(cnt)
	#print("Area: ",area)
	perimeter = cv2.arcLength(cnt,True)
	#print("Perimeter: ",perimeter)
	epsilon = 0.1*cv2.arcLength(cnt,True)
	approx = cv2.approxPolyDP(cnt,epsilon,True)
	#print("Contour Approx.: ",approx)
	hull = cv2.convexHull(cnt)
	#print("Hull: ",hull)
	convexity = cv2.isContourConvex(cnt)
	#print("Convexity: ",convexity)
	ellipse = cv2.fitEllipse(cnt)
	#cv2.ellipse(img,ellipse,(0,255,0),2)
	#print("Ellipse: ",ellipse)
	return H, area, perimeter, approx, hull, convexity, ellipse

def haralick(img):
	# this method computes the Haralick texture features
	texture = mahotas.features.haralick(img).mean(0)
	#print("Haralick Texture Features: ", texture)
	return texture
	
def orbDetect(img):	
	# Initiate STAR detector
	orb = cv2.ORB_create()
	# find the keypoints with ORB
	kp = orb.detect(img,None)
	# compute the descriptors with ORB
	kp, des = orb.compute(img, kp)
	# draw only keypoints location,not size and orientation
	#cv2.drawKeypoints(img,kp,img,color=(0,255,0), flags=0)
	#plt.imshow(img.copy()),plt.show()
	#print("Orb Descriptors: ", des)
	return des

def freakDetect(img,hessianThreshold=400):
	surfDetector = cv2.xfeatures2d.SURF_create(hessianThreshold) # manual threshold
	kp,des = surfDetector.detectAndCompute(img,None)
	#print("SURF Descriptors: ",des)
	#img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
	#plt.imshow(img2),plt.show() 
	#cv2.waitKey()
	freakExtractor = cv2.xfeatures2d.FREAK_create()
	kp2,des2= freakExtractor.compute(img,kp)
	#print("FREAK Descriptors: ",des2)
	#img3 = cv2.drawKeypoints(img,kp2,None,(255,0,0),4)
	#plt.imshow(img3),plt.show() 
	#cv2.waitKey()
	return des, des2
	
def appendAll(colour_set,H,area,perimeter,approx,hull,convexity,ellipse,texture,ORBdes,SURFdes,FREAKdes):
	obj_array = np.array(colour_set)
	obj_array = np.append(obj_array,H)
	obj_array = np.append(obj_array,area)
	obj_array = np.append(obj_array,perimeter)
	obj_array = np.append(obj_array,approx)
	obj_array = np.append(obj_array,hull)
	obj_array = np.append(obj_array,convexity)
	obj_array = np.append(obj_array,ellipse)
	obj_array = np.append(obj_array,texture)
	obj_array = np.append(obj_array,ORBdes)
	obj_array = np.append(obj_array,SURFdes)
	obj_array = np.append(obj_array,FREAKdes)
	return obj_array
