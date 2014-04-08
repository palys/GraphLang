'''
Created on 8 Apr 2014

@author: tpalys
'''
from scene.Component2D import Component2D

class Composite2D(object, Component2D):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.children = []

    def hasChildren(self):
        return True

    def addChild(self, component2D):
        self.children.append(component2D)

    def getChildren(self):
        return self.children
