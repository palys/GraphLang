'''
Created on 8 Apr 2014

@author: tpalys
'''
from src.scene.shape2d.primitives.Primitive import Primitive

class Rectangle(Primitive):
    '''
    classdocs
    '''


    def __init__(self, width, height, leftTopCornerX, leftTopCornerY):
        '''
        Constructor
        '''
        self.width = width
        self.height = height
        self.leftTopCornerX = leftTopCornerX
        self.leftTopCornerY = leftTopCornerY

    def __str__(self):
        return "Rectangle {0} {1} {2} {3}".format(self.width, self.height, self.leftTopCornerX, self.leftTopCornerY)

