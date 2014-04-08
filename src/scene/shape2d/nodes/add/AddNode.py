'''
Created on 8 Apr 2014

@author: tpalys
'''
from scene.shape2d.nodes.OperationNode2D import OperationNode2D

class AddNode(object, OperationNode2D):
    '''
    classdocs
    '''


    def __init__(self, primitive):
        '''
        Constructor
        '''
        self.primitive = primitive
