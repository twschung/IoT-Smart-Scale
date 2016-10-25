#from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np
import cv2
#import cv2.xfeatures2d
#import utils

def denoise(img):
	# This method uses non-local mean to denoise the image
	denoised = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	return denoised

def backgroundSubtraction(img, background):
	# This method extracts the foreground item from the background
	fgbg = cv2.createBackgroundSubtractorMOG2(1, 355, False)
	fgmask = fgbg.apply(background)
	fgmask = fgbg.apply(img)
	displayImg('fgmask', fgmask)
	blurbg = cv2.GaussianBlur(img,(15,15),0)
	displayImg('blurmask',blurbg)
	invmask = cv2.bitwise_not(fgmask)
	blurbg = cv2.bitwise_and(blurbg,blurbg,mask = invmask)
	subtracted = cv2.bitwise_and(img,img,mask = fgmask)
	subtracted = cv2.bitwise_or(subtracted,blurbg)
	displayImg('subtracted',subtracted)
	return subtracted, fgmask

def resizeImg(img):
	img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
	return img
	
def displayImg(title,img):
	# This method simply displays the image to the user
	cv2.imshow(title,img)
	cv2.waitKey(0)
	
def cropImg(img, mask):
	# This method crops out the black areas of the image
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	_,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
	_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[0]
	x,y,w,h = cv2.boundingRect(cnt)
	cropped = img[y:y+h,x:x+w]
	mask = mask[y:y+h,x:x+w]
	return cropped, mask
	
def findObjectCanny(img, mask):
	# This method implements the Canny Edge Detector where the thresholds are auto-calculated
	
	# Compute the median of the single channel pixel intensities
	#v = np.median(blur)
	# Apply automatic Canny edge detection using the computed median
	#lower = int(max(0, (1.0 - sigma) * v))
	#upper = int(min(255, (1.0 + sigma) * v))
	#img = cv2.GaussianBlur(img,(5,5),0)
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	displayImg('gray',gray)
	blurred = cv2.medianBlur(gray,5)
	displayImg('blurred',blurred)
	th = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	displayImg('th',th)
	kernel = np.ones((5,5),np.uint8)
	opened = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
	displayImg('opened',opened)
	edged = cv2.Canny(opened, 15, 255)
	displayImg('edged',edged)
	_,contours,_ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key = cv2.contourArea, reverse = True)
	cnts = contours[0]
	mask = np.zeros(gray.shape, dtype=np.uint8)
	cv2.drawContours(mask, [cnts], -1, (255, 0, 0), -1)
	displayImg('contoured',mask)
	object = cv2.bitwise_and(img,img,mask = mask)
	displayImg('object',object)
	object, mask = cropImg(object, mask)
	displayImg('cropped',object)

	return object, mask

def orbDetect(img):	
	# Initiate STAR detector
	orb = cv2.ORB_create()
	# find the keypoints with ORB
	kp = orb.detect(img,None)
	# compute the descriptors with ORB
	kp, des = orb.compute(img, kp)
	# draw only keypoints location,not size and orientation
	cv2.drawKeypoints(img,kp,img,color=(0,255,0), flags=0)
	plt.imshow(img),plt.show()
'''
def freakDetect(img,template):
	freakExtractor = cv2.xfeatures2d.FREAK_create()
	kp1,des1=freakExtractor.compute(img,None)
	kp2,des2=freakExtractor.compute(template,None)
	bf=cv2.BFMatcher()
	matches=bf.knnMatch(des1,des2,k=2)
	matches=sorted(matches,key=lambda x:x.distance)
	img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,flags=2)
	plt.imshow(img3),plt.imshow()
	cv2.waitKey(0)
'''
def KMean(img):
	# reshape the image to be a list of pixels
	Z = img.reshape((-1,3))
	# convert to np.float32
	Z = np.float32(Z)
	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	ret,label,center=cv2.kmeans(Z,4,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
	# Now convert back into uint8, and make original image
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	cv2.imshow('res2',res2)
	cv2.waitKey(0)

def colourHist(img, mask):
	color = ('b','g','r')
	norm_set = []
	for channel,col in enumerate(color):
		hist = cv2.calcHist([img],[channel],None,[32],[0,32])
		norm = cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX,-1)
		norm_set.append(norm);
		plt.plot(norm,color = col)
		plt.xlim([0,32])
	plt.title('Normalized histogram for color scale picture')
	plt.show()
	cv2.waitKey(0)
	norm_set = np.array(norm_set)
	np.reshape(norm_set, -1, 3)
	return norm_set
	
img = cv2.imread('apple.jpg')
background = cv2.imread('background.jpg')
img = resizeImg(img)
background = resizeImg(background)
displayImg('original',img)
subtracted, fgmask = backgroundSubtraction(img,background)
object, fgmaskc = findObjectCanny(subtracted, fgmask)
#orbDetect(object)
colour_set = colourHist(object, fgmaskc) #currently no use for fgmaskc
#freakDetect(object, img)
#KMean(object)
cv2.destroyAllWindows
#background = resizeImg(background)
#denoisedImg = denoise(img)
#denoisedBg = denoise(background)
