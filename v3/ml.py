# import cv2
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from sklearn.decomposition import PCA
import numpy as np
import time, os
import pickle
import _pickle as cpickle

def loadTrainingSet ():
	sampleSet = np.load('sampleSet.npy')
	responseSet = np.load('responseSet.npy')
	return sampleSet, responseSet

def saveTrainingSet (sampleSet, responseSet):
	np.save('sampleSet.npy',sampleSet)
	np.save('responseSet.npy',responseSet)

def addNewDataSet (newSampleSet, newResponseSet):
	try:
		sampleSet, responseSet = loadTrainingSet()
		sampleSet = np.vstack([sampleSet, newSampleSet])
		responseSet = np.hstack([responseSet,newResponseSet])
	except:
		sampleSet = newSampleSet
		responseSet = newResponseSet
	saveTrainingSet(sampleSet,responseSet)

class classifier():
	def __init__(self):
		self.Model = svm.SVC(C=1.0, kernel='poly', degree=3, probability=True)
	def load(self):
		self.Model = joblib.load('Model.dat')
	def train(self):
		sampleSet , responseSet = loadTrainingSet()
		self.Model.fit(sampleSet, responseSet)
		joblib.dump(self.Model, 'Model.dat')
	def predict(self, sample):
		return self.Model.predict(sample)
	def predict_prob(self, sample):
		proba = self.Model.predict_proba(sample)
		result =[];
		print(len(proba));
		for k in range (0,len(proba[0])):
			x = (k+1,proba[0][k])
			result.append(x)
		return result
