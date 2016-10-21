import cv2
import numpy as np

def loadTrainingSet ():
	traningSet = np.load('traningSet.npy')
	return traningSet

def saveTrainingSet (traningSet):
	np.save('traningSet.npy',traningSet)
	
def addNewDataSet (newSet):
	traningSet = loadTrainingSet()
	traningSet = np.vstack([traningSet,newSet])
	saveTrainingSet(traningSet)
	
def readTrainingSet ():
	traningSet = loadTrainingSet()
	labelSet = traningSet[:,0]
	sampleSet = traningSet[:,1:(traningSet.shape[1])]
	return labelSet, sampleSet
	
	
newSet = [1,2,3,4]
addNewDataSet(newSet)
labelSet , sampleSet = readTrainingSet()
print (labelSet)
print (sampleSet)

