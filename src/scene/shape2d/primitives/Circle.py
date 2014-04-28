'''
Created on 8 Apr 2014

@author: tpalys
'''
from src.scene.shape2d.primitives.Primitive import Primitive

class Circle(object, Primitive):
    '''
    classdocs
    '''


    def __init__(self, centerX, centerY, radius):
        '''
        Constructor
        '''
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius

    def __str__(self):
        return "Circle {0} {1} {2}".format(self.centerX, self.centerY, self.radius)