import cv2
import numpy as np

def threshold (img_filename):
	img = cv2.imread(img_filename,0)
	#cv2.cvtColor(img,img_gray,CV_RGB2GRAY)
	th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	th2 = th1 * img
	showImage(img)
	showImage(th1)
	showImage(th2)
	return

def showImage (img):
	cv2.imshow("done",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return

