import sys
import os
import random
import copy
from time import clock

sys.path.append(os.getcwd())
from Evaluate.Evaluate import Evaluate
from Data.Data import Data
from Point.Point import Point

label = 0

def makePoint(data, eps, minPts):
	length = len(data.data)
	for i in range(length):
		nearPointNum = 0
		for j in range(length):
			if data.data[i].getEuclidDis(data.data[i], data.data[j]) < eps:
				nearPointNum += 1
		if nearPointNum > minPts:
			data.data[i].type = 1
	return data


def merge(data, eps):
    global label
    bfs = []
    head = 0
    tail = 0
    length = len(data.data)
    for i in range(length):
        if data.data[i].type and data.data[i].label == 0:
            data.data[i].label = label
            head = 0
            tail = 1
            bfs = []
            bfs.append(i)
            while head < tail:
                for j in range(length):
                    if data.data[j].label == 0 and data.data[i].getEuclidDis(data.data[i], data.data[j]) < eps:
                        data.data[j].label = label
                        if data.data[j].type:
                            tail += 1
                            bfs.append(j)
                head += 1
            label += 1
    return data


def getCluster(data):
    global label
    cluster = []
    for i in range(label):
        cluster.append([])
    for i in range(len(data.data)):
        cluster[data.data[i].label].append(data.data[i])
    return cluster


def DbScanRun(data, eps, minPts):
    global label
    begin = clock()
    label = 1
    data = makePoint(data, eps, minPts)
    data = merge(data, eps)
    end = clock()
    cluster = getCluster(data)
    ev = Evaluate()
    ev.EvaluateRun(data, cluster)
    print ("number of cluster:%d" %(label))
    print ("purity is %f" %(ev.purity))
    print ("FScore is %f" %(ev.FScore))
    print ("time used: %d s" %(end - begin))


if __name__ == '__main__':
    data = Data()
    DbScanRun(data, 4, 5)