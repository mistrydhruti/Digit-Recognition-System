import sklearn
from sklearn.externals import joblib
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np
from collections import Counter
from sklearn.datasets import fetch_openml



mnist=fetch_openml('mnist_784')
features = np.array(mnist.data, 'int16')
labels = np.array(mnist.target,'int')
list_hog_fd = []
for feature in features:
    fd = hog(feature.reshape((28,28)), orientations=9, pixels_per_cell=(14,14),cells_per_block=(1,1))
    list_hog_fd.append(fd)
hog_features = np.array(list_hog_fd,'float64')

print("Count of digits in dataset", Counter(labels))

clf = LinearSVC()

clf.fit(hog_features,labels)

joblib.dump(clf, "digits_cls.pkl", compress=3)
