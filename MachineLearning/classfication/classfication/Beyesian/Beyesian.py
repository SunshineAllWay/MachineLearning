import sys
import os
import copy
sys.path.append(os.getcwd())

from Data.Data import Data

def getPC(data, r):
    hit = 0
    for i in range(data.trainingSize):
        if cmp(data.trainingSet[i][8], r) == 0:
            hit = hit + 1
    return float(hit) / float(data.trainingSize)

def getPAC(data, v, r):
    nc = 0
    nac = 0
    for i in range(data.trainingSize):
        match = 1
        if cmp(data.trainingSet[i][8], r):
            continue
        else:
            nc = nc + 1
            for j in range(8):
                if cmp(data.trainingSet[i][j], v[j]):
                    match = 0
            if match:
                nac = nac + 1
    return float(nac) / float(nc)


def BeyesianRun(data):
    testNum = 0
    data.matchSize = 0
    for it in data.testingSet:
        testNum = testNum + 1
        v = copy.deepcopy(it)
        v.pop()
        correctClass = it[8]
        resultClass = 'yes'
        pc1 = getPC(data, 'yes')
        pc2 = getPC(data, 'no')
        pac1 = getPAC(data, v, 'yes')
        pac2 = getPAC(data, v, 'no')
        prop1 = pac1 * pc1
        prop2 = pac2 * pc2
        if prop1 < prop2:
            resultClass = 'no'
        if cmp(resultClass, correctClass) == 0:
            data.matchSize = data.matchSize + 1
        print ("testID: %d" %(testNum)) 
        print ("correct rate is %f" %(float(data.matchSize)/float(testNum)))


if __name__ == '__main__':
    data = Data()
    BeyesianRun(data)
    print 1

                