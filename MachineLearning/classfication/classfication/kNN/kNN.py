import sys
import os
import copy
sys.path.append(os.getcwd())

from Data.Data import Data

def DistanceJudge(v1, v2):
    dis = 0
    for i in range(len(v1)):
        if cmp(v1[i], v2[i]):
            dis = dis + 1
    return dis
                
def kNNRun(data, k):
    testNum = 0;
    for it1 in data.testingSet:
        testNum = testNum + 1
        disList = []
        for it2 in data.trainingSet:
            v1 = copy.deepcopy(it1)
            v2 = copy.deepcopy(it2)
            v1.pop()
            v2.pop()
            dis = DistanceJudge(v1, v2)
            disList.append([dis, it2[len(it1)-1]])
        disList.sort(lambda x, y:cmp(x[0], y[0]))
        num1 = 0
        num2 = 0
        for i in range(k):
            if cmp(disList[i][1], 'no') == 0:
                num1 = num1 + 1
            else:
                num2 = num2 + 1
        if num1 > num2:
            result = 'no'
        else:
            result = 'yes'
        if cmp(result, it1[len(it1)-1]) == 0:
            data.matchSize = data.matchSize + 1
        print ("testID: %d" %(testNum)) 
        print ("correct rate is %f" %(float(data.matchSize)/float(testNum)))
    return 


if __name__ == '__main__':
    data = Data()
    kNNRun(data, 3)

