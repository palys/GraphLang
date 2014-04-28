'''
Created on 7 Apr 2014

@author: tpalys
'''

class Scene(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.components2D = []

    def addComponent(self, component2D):
        self.components2D.append(component2D)

    def __str__(self):
        s = "------>\nscene({0}, {1})\n".format(self.width, self.height)
        for x in self.components2D:
            s += str(x) + "\n"
        return s
