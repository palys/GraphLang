'''
Created on 8 Apr 2014

@author: tpalys
'''

from scene.shape2d.nodes.transformation.TransformationNode2D import TransformationNode2D

class TranslationNode(object, TransformationNode2D):
    '''
    classdocs
    '''


    def __init__(self, vecX, vecY):
        '''
        Constructor
        '''
        self.vecX = vecX
        self.vecY = vecY
