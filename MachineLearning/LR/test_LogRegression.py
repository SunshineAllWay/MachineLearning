#################################################  
# logRegression: Logistic Regression  
# Author : zouxy  
# Date   : 2014-03-02  
# HomePage : http://blog.csdn.net/zouxy09  
# Email  : zouxy09@qq.com  
#################################################  
  
from numpy import *  
import matplotlib.pyplot as plt  
import time  
import os
from logRegression import *
  
def loadData():  
    train_x = []  
    train_y = []  
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'data.txt')
    fileIn = open(file_path)  
    for line in fileIn.readlines():  
        lineArr = line.strip('\n').split('\t')  
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])  
        train_y.append(float(lineArr[2]))  
    return mat(train_x), mat(train_y).transpose()  
  
  
## step 1: load data  
print "step 1: load data..."  
train_x, train_y = loadData()  
test_x = train_x
test_y = train_y  
  
## step 2: training...  
print "step 2: training..."  
opts = {'alpha': 0.01, 'maxIter': 200, 'optimizeType': 'gradDescent'}  
optimalWeights = trainLogRegres(train_x, train_y, opts)  
  
## step 3: testing  
print "step 3: testing..."  
accuracy = testLogRegres(optimalWeights, test_x, test_y)  
  
## step 4: show the result  
print "step 4: show the result..."    
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)  
showLogRegres(optimalWeights, train_x, train_y)   
