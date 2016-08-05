import sys
import os
import math
from time import clock

class Point:
    def __init__(self, latitude, longtitude, location):
        self.latitude = latitude
        self.longtitude = longtitude
        self.location = location
        self.label = 0
        self.type = 0

    def getEuclidDis(self, p1, p2):
        latitudeDis = p1.latitude - p2.latitude
        longtitudeDis = p1.longtitude - p2.longtitude
        return (latitudeDis * latitudeDis + longtitudeDis * longtitudeDis)
