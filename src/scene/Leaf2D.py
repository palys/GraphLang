'''
Created on 8 Apr 2014

@author: tpalys
'''
from scene import Component2D

class Leaf2D(object, Component2D):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

    def hasChildren(self):
        return False

    def getChildren(self):
        return []