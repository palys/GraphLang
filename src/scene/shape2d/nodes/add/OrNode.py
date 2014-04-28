'''
Created on 8 Apr 2014

@author: tpalys
'''
from src.scene.shape2d.nodes.add.AddNode import AddNode

class OrNode(AddNode):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

    def __str__(self):
        return "Or \n{0}".format(str(self.primitive))