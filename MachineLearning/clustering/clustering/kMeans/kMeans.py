import sys
import os
import random
import copy
from time import clock

sys.path.append(os.getcwd())
from Evaluate.Evaluate import Evaluate
from Data.Data import Data


def getNearestCluster(means, p):
    minDis = (means[0][0] - p.latitude) * (means[0][0] - p.latitude) + (means[0][1] - p.longtitude) * (means[0][1] - p.longtitude)
    label = 1
    for i in range(1, len(means)):
        tempDis = (means[i][0] - p.latitude) * (means[i][0] - p.latitude) + (means[i][1] - p.longtitude) * (means[i][1] - p.longtitude)
        if minDis > tempDis:
            minDis = tempDis
            label = i + 1
    return label


def getMeans(means, cluster, k):
    means = []
    for i in range(k):
        means.append([0, 0])
    for i in range(len(cluster)):
        averageLatitude = 0;
        averageLongtitude = 0;
        for j in range(len(cluster[i])):
            averageLatitude = averageLatitude + cluster[i][j].latitude
            averageLongtitude = averageLongtitude + cluster[i][j].longtitude
        if len(cluster[i]) == 0:
            continue
        else:
            averageLatitude = averageLatitude / len(cluster[i])
            averageLongtitude = averageLongtitude / len(cluster[i])
            means[i][0] = averageLatitude
            means[i][1] = averageLongtitude
    return means


def getCluster(data, cluster, k):
    cluster = []
    for i in range(k):
        cluster.append([])
    for i in range(len(data.data)):
        cluster[data.data[i].label - 1].append(data.data[i])
    return cluster

def kMeansRun(data, k, empty):
    cluster = []
    means = []
    change = -1
    times = 0
    begin = clock()
    for i in range(len(data.data)):
        data.data[i].label = i % k + 1
    cluster = getCluster(data, cluster, k)
    means = getMeans(means, cluster, k)
    while 1:
        change = 0
        meansCopy = copy.deepcopy(means)
        for p in data.data:
            label = getNearestCluster(means, p)
            if label != p.label:
                change = change + 1
                p.label = label
        cluster = getCluster(data, cluster, k)
        means = getMeans(means, cluster, k)
        times = times + 1
        if empty == 0:
            #handle empty cluster
            clusterDis = []
            for i in range(len(data.data)):
                m = data.data[i]
                dis = (m.latitude - means[m.label - 1][0]) * (m.latitude - means[m.label - 1][0]) + (m.longtitude - means[m.label - 1][1]) * (m.longtitude - means[m.label - 1][1])
                clusterDis.append([i, dis])
            clusterDis.sort(lambda x, y: cmp(y[1], x[1]))
            emptyClusterNum = 0
            for i in range(len(cluster)):
                if len(cluster[i]) == 0:
                    if len(cluster[data.data[emptyClusterNum].label - 1]) == 1:
                        emptyClusterNum = emptyClusterNum + 1
                        i = i - 1
                        continue
                    else:
                        data.data[emptyClusterNum].label = i + 1
                        change = change + 1
                        emptyClusterNum = emptyClusterNum + 1
            cluster = getCluster(data, cluster, k)
            means = getMeans(means, cluster, k)
        print("iteration number: %d" %(times))
        print("change = %d" %(change))
        if float(change) / float(len(data.data)) < 0.001:
            break
    clusterNum = 0
    end = clock()
    for c in cluster:
        if len(c) != 0:
            clusterNum = clusterNum + 1
    print ("iterate %d times" %(times))
    print ("create %d clusters" %(clusterNum))
    ev = Evaluate()
    ev.EvaluateRun(data, cluster)
    print ("purity is %f" %(ev.purity))
    print ("FScore is %f" %(ev.FScore))
    print ("time used: %d s" %(end - begin))


if __name__ == '__main__':
    data = Data()
    kMeansRun(data, 3, 1)