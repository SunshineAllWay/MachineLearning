from numpy import *
import os
import matplotlib.pyplot as plt

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip('\n').split(delim) for line in fr.readlines()]
    datArr = [map(float,line) for line in stringArr]
    return mat(datArr)

def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
    print("meanVals")
    print(meanVals)
    meanRemoved = dataMat - meanVals #remove mean
    covMat = cov(meanRemoved, rowvar=0)
    print("covMat")
    print(covMat)
    eigVals,eigVects = linalg.eig(mat(covMat))
    print("eigVals")
    print(eigVals)
    print("eigVects")
    print(eigVects)
    eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
    print("eigValInd")
    print(eigValInd)
    eigValsInd = eigValInd[::-1][:topNfeat]
    #eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
    print("eigValInd")
    print(eigValInd)
    redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest
    print("redEigVects")
    print(redEigVects)
    lowDDataMat = meanRemoved * redEigVects#transform data into new dimensions
    print("lowDDataMat")
    print(lowDDataMat)
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

def plotBestFit(dataSet1,dataSet2):      
    dataArr1 = array(dataSet1)
    dataArr2 = array(dataSet2)
    n = shape(dataArr1)[0] 
    n1=shape(dataArr2)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    xcord3=[];ycord3=[]
    j=0
    for i in range(n):
        
            xcord1.append(dataArr1[i,0]); ycord1.append(dataArr1[i,1])
            xcord2.append(dataArr2[i,0]); ycord2.append(dataArr2[i,1])
                   
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()    




if __name__=='__main__':
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'test.txt')
    mata=loadDataSet(file_path)  
    a,b = pca(mata, 2)
    plotBestFit(a,b)