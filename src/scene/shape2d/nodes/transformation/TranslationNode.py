'''
Created on 8 Apr 2014

@author: tpalys
'''

from src.scene.shape2d.nodes.transformation.TransformationNode2D import TransformationNode2D

class TranslationNode(TransformationNode2D):
    '''
    classdocs
    '''


    def __init__(self, vecX, vecY):
        '''
        Constructor
        '''
        self.vecX = vecX
        self.vecY = vecY

    def __str__(self):
        return "Translation {0} {1}".format(self.vecX, self.vecY)
