#################################################  
# SVM: support vector machine  
# Author : zouxy  
# Date   : 2013-12-12  
# HomePage : http://blog.csdn.net/zouxy09  
# Email  : zouxy09@qq.com  
#################################################  
  
from numpy import *  
import SVM  
import os
  
################## test svm #####################  
## step 1: load data  
print "step 1: load data..."  
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'data.txt')
fileIn = open(file_path, 'r')  
dataSet = []
labels = []
for line in fileIn.readlines():  
    lineArr = line.strip('\n').split('\t')  
    dataSet.append([float(lineArr[0]), float(lineArr[1])])  
    labels.append(float(lineArr[2]))  
  
dataSet = mat(dataSet)  
labels = mat(labels).T  
train_x = dataSet[0:189, :]  
train_y = labels[0:189, :]  
test_x = dataSet[188:218, :]  
test_y = labels[188:218, :]  
  
## step 2: training...  
print "step 2: training..."  
C = 0.6  
toler = 0.001  
maxIter = 50  
svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0))  
  
## step 3: testing  
print "step 3: testing..."  
accuracy = SVM.testSVM(svmClassifier, test_x, test_y)  
  
## step 4: show the result  
print "step 4: show the result..."    
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)  
#SVM.showSVM(svmClassifier)  