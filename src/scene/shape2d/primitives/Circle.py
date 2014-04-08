'''
Created on 8 Apr 2014

@author: tpalys
'''
from scene.shape2d.primitives.Primitive import Primitive

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