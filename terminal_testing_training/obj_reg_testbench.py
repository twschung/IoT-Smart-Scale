import obj_recognition
import svm
import numpy as np

currentPath = "forground_2.jpg"
currentBackgroundPath = "background_2.jpg"
imgFeature = obj_recognition.main(currentPath,currentBackgroundPath)
print (imgFeature)
print (imgFeature.shape)
print (imgFeature.dtype)

clf = svm.classifier()
clf.load()
print (clf.predict(imgFeature))
print (clf.predict_prob(imgFeature))

currentPath = "forground_3.jpg"
currentBackgroundPath = "background_3.jpg"
imgFeature = obj_recognition.main(currentPath,currentBackgroundPath)
print (imgFeature)
print (imgFeature.shape)
print (imgFeature.dtype)

clf = svm.classifier()
clf.load()
print (clf.predict(imgFeature))
print (clf.predict_prob(imgFeature))
