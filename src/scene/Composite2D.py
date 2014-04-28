'''
Created on 8 Apr 2014

@author: tpalys
'''
from src.scene.Component2D import Component2D

class Composite2D(Component2D):
    '''
    classdocs
    '''
    children = []

    def __init__(self):
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

    def __str__(self):
        s = ""
        print "$"
        for x in self.children:
            print "!"
            s.join("\n").join(str(x))
        return s
