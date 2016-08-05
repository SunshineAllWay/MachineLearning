import sys
import os
from time import clock

sys.path.append(os.getcwd())
from Point.Point import Point

class Data:
    def __init__(self):
        start = clock()
        BASE_DIR = os.path.dirname(__file__)
        file_path = os.path.join(BASE_DIR, 'input/data.txt')
        txtfile = open(file_path, "r")
        data = []
        input = []
        for line in txtfile:
            input.append(list(line.strip('\n').split('\t')))
        for i in range(len(input)):
            latitude = float(input[i][0])
            longtitude = float(input[i][1])
            location = int(input[i][2])
            data.append(Point(latitude, longtitude, location))
        self.data = data





