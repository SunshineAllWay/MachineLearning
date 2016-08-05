import sys
import os
import random
import copy
from time import clock

sys.path.append(os.getcwd())
from Data.Data import Data

class Evaluate:
    def __init__(self):
        self.purity = 0
        self.FScore = 0


    def EvaluateRun(self, data, cluster):
        self.purity = self.getPurity(data, cluster)
        self.FScore = self.getFScore(data, cluster)


    def getPurity(self, data, cluster):
        totalCount = 0;
        for i in range(len(cluster)):
            locationDict = {}
            for m in cluster[i]:
                if locationDict.has_key(m.location):
                    locationDict[m.location] = locationDict[m.location] + 1
                else:
                    addDict = {m.location: 1}
                    locationDict.update(addDict)
            maxCount = 0
            for (location, count) in locationDict.items():
                if maxCount < count:
                    maxCount = count
            totalCount = totalCount + maxCount
        return float(totalCount) / float(len(data.data))
    
    def getFScore(self, data, cluster):
        TP = 0  
        TN = 0 
        FP = 0  
        FN = 0 
        TPFP = 0 #TP+FP
        TNFN = 0 #TN+FN
        totalResult = {}
        result = []
        
        for i in range(len(cluster)):
            result.append({})
            for j in range(len(cluster[i])):
                if result[i].has_key(cluster[i][j].location):
                    result[i][cluster[i][j].location] += 1
                else:
                    result[i].update({cluster[i][j].location:1})
        tmpResult = {}
        tmpResult1 = {}
        tmpResult2 = {}
     
        for i in range(len(cluster)):
            if len(result[i].items()) == 0:
                continue
            TPFP += len(cluster[i]) * (len(cluster[i]) - 1) / 2
            tmpResult = result[i]
            for (location, num) in tmpResult.items():
                TP += num * (num - 1) / 2
        FP = TPFP - TP

        for i in range(len(cluster)):
            for j in range(len(cluster)):
                if i != j:
                    TNFN += len(cluster[i]) * len(cluster[j])
        TNFN /= 2
        for i in range(len(cluster)):
            for j in range(len(cluster[i])):
                if totalResult.has_key(cluster[i][j].location):
                    totalResult[cluster[i][j].location] += 1
                else:
                    totalResult.update({cluster[i][j].location:1})
        for (location, num) in totalResult.items():
            for i in range(len(cluster)):
                for j in range(len(cluster)):
                    if i != j and result[i].has_key(location) and result[j].has_key(location):
                        FN += result[i][location] * result[j][location]
        TN = TNFN - FN
        precision = float(TP) / float(FP + TP)
        recall = float(TP) / float(FP + FN)
        FScore = 2 * recall * precision / (recall + precision)
        return FScore