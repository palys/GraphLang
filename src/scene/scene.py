'''
Created on 3 Jun 2014

@author: tpalys
'''

class Scene(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.children = []

    def add(self, element):
        self.children.append(element)

    def extend(self, elements):
        self.children.extend(elements)

    def __str__(self):
        s = "({0}, {1})\n".format(self.width, self.height)

        for x in self.children:
            s += str(x) + "\n"

        return s

class Color(object):

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return "Color: {0} {1} {2}".format(self.red, self.green, self.blue)

class Primitive(object):
    pass

class Rectangle(Primitive):

    def __init__(self, left, right, bottom, top):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return "Rectangle: {0} {1} {2} {3}".format(self.left, self.top, self.right, self.bottom)

class Transformation(object):
    pass

class Rotation(Transformation):

    def __init__(self, angle):
        self.angle = angle

    def __str__(self):
        return "Rotation: {0}".format(self.angle)

class Translation(Transformation):

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __str__(self):
        return "Translation: {0} {1}".format(self.dx, self.dy)


