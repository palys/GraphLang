'''
Created on 8 Apr 2014

@author: tpalys
'''
from src.scene.Composite2D import Composite2D
from src.scene.Leaf2D import Leaf2D

class OperationList2D(Composite2D):
    '''
    classdocs
    '''


    def __init__(self, param):
        '''
        Constructor
        '''
        self.addChildren(param)

    def addChildren(self, children):
        toIterate = children
        if isinstance(children, OperationList2D):
            toIterate = children.getChildren()
        if isinstance(children, Leaf2D):
            self.addChild(children)
        else:
            for x in toIterate:
                self.addChild(x)

    def __str__(self):
        s = ""
        print "$"
        for x in self.children:
            print x
            s += str(x) + "\n"
        return s