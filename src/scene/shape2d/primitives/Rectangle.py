'''
Created on 8 Apr 2014

@author: tpalys
'''
from scene.shape2d.primitives.Primitive import Primitive

class Rectangle(object, Primitive):
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

