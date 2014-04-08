'''
Created on 7 Apr 2014

@author: tpalys
'''

class Scene(object):

    def __init__(self, params):
        self.components2D = []

    def addComponent(self, component2D):
        self.components2D.append(component2D)
