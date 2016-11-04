import os
import numpy as np

def sim(imgPath):
	filename = os.path.basename(imgPath)
	time, imgID = filename.split("_")
	imgID, extend = imgID.split(".")
	if (imgID == "1"):
		feature = np.array([0.9876,0.5374,0.1243,0.7890], dtype = np.float32)
	elif (imgID == "2"):
		feature = np.array([0.6543,0.6789,0.9867,0.6215], dtype = np.float32)
	elif (imgID == "3"):
		feature = np.array([0.2467,0.1098,0.8909,0.4653], dtype = np.float32)
	elif (imgID == "4"):
		feature = np.array([0.1789,0.8098,0.4987,0.9657], dtype = np.float32)
	elif (imgID == "5"):
		feature = np.array([0.2080,0.3677,0.1243,0.1082], dtype = np.float32)
	return feature
