'''
Created on 20 kwi 2014

@author: tpalys
'''

from src.scene.shape2d.nodes.OperationNode2D import OperationNode2D

class ColorNode(OperationNode2D):
    '''
    classdocs
    '''


    def __init__(self, r, g, b):
        '''
        Constructor
        '''
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return "Color {0} {1} {2}".format(self.r, self.g, self.b)