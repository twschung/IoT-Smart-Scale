import obj_recognition
import svm
import numpy as np

currentPath = "forground.jpg"
currentBackgroundPath = "background.jpg"
imgFeature = obj_recognition.main(currentPath,currentBackgroundPath)
print (imgFeature)
print (imgFeature.shape)
print (imgFeature.dtype)

clf = svm.Tree()
clf.load()
print (clf.predict(imgFeature))
print (clf.predict_prob(imgFeature))

#~
#~ currentPath = "/home/pi/Desktop/FTP/imageUploaded/newItem/1480363072.310857.jpg"
#~ currentBackgroundPath = "/home/pi/Desktop/FTP/imageUploaded/newItem/backgroundImage/1480363072.310857.jpg"
#~ imgFeature = obj_recognition.main(currentPath,currentBackgroundPath)
#~ print (imgFeature)
#~ print (imgFeature.shape)
#~ print (imgFeature.dtype)
#~
#~ clf = svm.SVM()
#~ clf.load()
#~ inputNewImg = "/home/pi/Desktop/v3/1480366925.8335626.jpg"
#~ inputNewBackgroundImg = "/home/pi/Desktop/v3/backgroundImage/1480366925.8335626.jpg"
#~ inputNewImg = "/home/pi/Desktop/v2/1480363072.310857.jpg"
#~ inputNewBackgroundImg = "/home/pi/Desktop/v2/backgroundImage/1480363072.310857.jpg"
#~ imgFeature = obj_recognition.main(inputNewImg,inputNewBackgroundImg)
#~ imgFeature = np.nan_to_num(imgFeature)
#~ imgFeature_1 = np.array([imgFeature])
#~ clfResult = clf.predict(imgFeature)
#~ print(clfResult)
#~ clfResult = clf.predict_prob(imgFeature)
#~ print(clfResult)
