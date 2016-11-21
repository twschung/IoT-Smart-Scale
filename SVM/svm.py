# import cv2
from sklearn import svm
from sklearn.externals import joblib
from sklearn.decomposition import PCA
import numpy as np
import time, os


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

class SVM():
	def __init__(self):
		self.model = svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='auto', \
		coef0=0.0, shrinking=True, probability=True, tol=0.001, cache_size=200, \
		class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None, \
		random_state=None)
		self.PCA = PCA(n_components = 500)
	def load(self):
		self.model = joblib.load('SVM.dat')
		self.PCA = joblib.load('PCA.dat')
	def train(self):
		sampleSet , responseSet = loadTrainingSet()
		self.PCA.fit(sampleSet)
		reduced_dimen_sampleSet = self.PCA.transform(sampleSet)
		self.model.fit(sampleSet, responseSet)
		joblib.dump(self.model, 'SVM.dat')
		joblib.dump(self.PCA, 'PCA.dat')
	def predict(self, sample):
		reduced_dimen_sample = self.PCA.transform(sample)
		return self.model.predict(sampleSet)
	def predict_prob(self, sample):
		reduced_dimen_sample = self.PCA.transform(sample)
		return self.model.predict_proba(sampleSet)
