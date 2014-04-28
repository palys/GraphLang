'''
Created on 20 kwi 2014

@author: tpalys
'''
from src.scene.shape2d.nodes.transformation.TransformationNode2D import TransformationNode2D

class RotationNode(TransformationNode2D):
    '''
    classdocs
    '''


    def __init__(self, angle):
        '''
        Constructor
        '''
        self.angle = angle

    def __str__(self):
        return "Rotation {0}".format(self.angle)
