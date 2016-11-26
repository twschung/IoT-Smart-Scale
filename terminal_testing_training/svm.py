# import cv2
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
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

class classifier():
	def __init__(self):
		# self.SVCModel = svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='auto', \
		# coef0=0.0, shrinking=True, probability=True, tol=0.001, cache_size=200, \
		# class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovo', \
		# random_state=None)
		# self.TreeModel = tree.DecisionTreeClassifier()
		self.TreeModel = RandomForestClassifier(n_estimators=30)
		# self.PCA = PCA(n_components = 15)
	def load(self):
		# self.SVCModel = joblib.load('SVC.dat')
		self.TreeModel = joblib.load('Tree.dat')
		# self.PCA = joblib.load('PCA.dat')
	def train(self):
		sampleSet , responseSet = loadTrainingSet()
		# self.PCA.fit(sampleSet)
		# reduced_dimen_sampleSet = self.PCA.transform(sampleSet)
		# self.SVCModel.fit(reduced_dimen_sampleSet, responseSet)
		# self.TreeModel.fit(reduced_dimen_sampleSet, responseSet)
		self.TreeModel.fit(sampleSet, responseSet)
		# joblib.dump(self.SVCModel, 'SVC.dat')
		joblib.dump(self.TreeModel, 'Tree.dat')
		# joblib.dump(self.PCA, 'PCA.dat')
	def predict(self, sample):
		# reduced_dimen_sample = self.PCA.transform(sample)
		return self.TreeModel.predict(sample)
	def predict_prob(self, sample):
		# reduced_dimen_sample = self.PCA.transform(sample)
		return self.TreeModel.predict_proba(sample)
		# return self.SVCModel.predict_proba(reduced_dimen_sample)
