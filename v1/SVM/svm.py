import cv2
import numpy as np

def initalTrainingSet():
	newSampleSet = np.array([[0.9,0.8,0.1,0.3],[1.1,1,0.05,0.2],[0.4,0.2,0.3,0.4],[0.4,0.2,0.3,0.4]], dtype=np.float32)
	newResponseSet = np.array([3,3,1,1], dtype=np.int)
	saveTrainingSet(newSampleSet, newResponseSet)
	

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
	
class StatModel(object):
	def load(self, fn):
		self.model.load(fn)
	def save(self, fn):
		self.model.save(fn)
	
class SVM(StatModel):
	def __init__(self, C = 1, gamma = 0.5):
		self.model = cv2.ml.SVM_create()
		self.model.setGamma(gamma)
		self.model.setC(C)
		self.model.setKernel(cv2.ml.SVM_RBF)
		self.model.setType(cv2.ml.SVM_C_SVC)
	def train(self):
		sampleSet , responseSet = loadTrainingSet()
		self.model.train(sampleSet, cv2.ml.ROW_SAMPLE, responseSet)
	def predict(self, sample):
		return self.model.predict(sample)
	

# samples = np.array(np.random.random((4,2)), dtype = np.float32)
# y_train = np.array([1.,0.,0.,1.], dtype = np.float32)
# print (samples.shape)
# print (samples)
# print (y_train.shape)
# print (y_train)
	
# initalTrainingSet()
	
# newSampleSet = np.array([0.2,0.8,0.6,0.1], dtype=np.float32)
# newResponseSet = np.array([2], dtype=np.int)
# newSampleSet = np.array([0.8,0.2,0.1,0.9], dtype=np.float32)
# newResponseSet = np.array([3], dtype=np.int)
# addNewDataSet(newSampleSet,newResponseSet)

# sampleSet , responseSet = loadTrainingSet()

# print (sampleSet.dtype)
# print (sampleSet.shape)
# print (sampleSet)
# print (responseSet.dtype)
# print (responseSet.shape)
# print (responseSet)

# print (newSampleSet.shape)
# print (newSampleSet)
# print (newResponseSet.shape)
# print (newResponseSet)

# clf = SVM(C=2.67, gamma=5.383)
# clf.train()
# clf.save('trainedSVM.dat')

clf = cv2.ml.SVM_load('trainedSVM.dat')
sample = np.array([[0.9,0.1,0.2,0.8]], dtype=np.float32)
print (sample.shape)
result = clf.predict(sample)
print(result)

# sample = [2,3,3]

