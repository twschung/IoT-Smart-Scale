from sklearn import svm
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import numpy as np


sampleSet = np.load('sampleSet.npy')
responseSet = np.load('responseSet.npy')
# trainingRS = np.load('trainingRS.npy')
# trainingSS = np.load('trainingSS.npy')
# validationRS = np.load('validationRS.npy')
# validationSS = np.load('validationSS.npy')

trainingSS , validationSS , trainingRS , validationRS = train_test_split(sampleSet, responseSet, test_size=0.33, random_state=42)



clf = []
clf.append(tree.DecisionTreeClassifier())
clf.append(RandomForestClassifier(n_estimators=25))
clf.append(BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5))
clf.append(svm.LinearSVC())
clf.append(svm.SVC(C=1.0, kernel='linear'))
clf.append(svm.SVC(C=1.0, kernel='rbf', gamma=0.7))
clf.append(svm.SVC(C=1.0, kernel='poly', degree=3))

for x in range (0,len(clf)):
    clf[x].fit(trainingSS,trainingRS)
    print ("score: ",clf[x].score(validationSS,validationRS))
    # for y in range (0,validationRS.shape[0]):
    #     print (validationRS[y], " - " , clf[x].predict(validationSS[y]))
