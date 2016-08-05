import sys
import os
from time import clock

class Data:

    def __init__(self):
        start = clock()
        BASE_DIR = os.path.dirname(__file__)
        file_path = os.path.join(BASE_DIR, 'input/bank-full.csv')
        csvfile = open(file_path, "r")
        input = []
        for line in csvfile:
            input.append(list(line.strip().replace('\"', '').split(';')))
        originAttribute = [];
        for i in range(1, len(input)):
            originAttribute.append([])
            originAttribute[i - 1] = []
            for j in range(len(input[i])):
                originAttribute[i - 1].append(input[i][j])
        self.originAttribute = originAttribute

        attribute = []
        for i in range(len(originAttribute)):
            attribute.append([])
            for j in range(8):
                if j == 0:
                    if originAttribute[i][j].isdigit():
                        t = int(originAttribute[i][j])
                        if t < 35:
                            attribute[i].append(1)
                        elif t >= 35 and t <= 45:
                            attribute[i].append(2)
                        else:
                            attribute[i].append(3)
                    else:
                        attribute[i].append(1)
                elif j == 5:
                    if originAttribute[i][j].isdigit():
                        t = int(originAttribute[i][j])
                        if t < 200:
                            attribute[i].append(1)
                        elif t >= 200 and t <= 1000:
                            attribute[i].append(2)
                        else:
                            attribute[i].append(3)
                    else:
                        attribute[i].append(1)
                else:
                    attribute[i].append(originAttribute[i][j])
            attribute[i].append(originAttribute[i][len(originAttribute[i])-1])
        self.attribute = attribute

        trainingSize = len(attribute) / 5 * 4
        trainingSet = []
        testingSet = []
        for i in range(len(attribute)):
            if i < trainingSize:
                trainingSet.append(attribute[i])
            else:
                testingSet.append(attribute[i])

        self.trainingSize = trainingSize
        self.trainingSet = trainingSet
        self.testingSet = testingSet
        self.testingSize = len(testingSet)
        self.matchSize = 0
        end = clock()
        print ("import data: %d s" %(end - start))






    