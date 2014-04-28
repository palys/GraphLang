'''
Created on 8 Apr 2014

@author: tpalys
'''
from src.scene.shape2d.nodes.OperationNode2D import OperationNode2D

class AddNode(OperationNode2D):
    '''
    classdocs
    '''

    primitive = None

    def __init__(self, primitive):
        '''
        Constructor
        '''
        self.primitive = primitive

    def __str__(self):
        return "Add... primitive is {0}".format(str(self.primitive))