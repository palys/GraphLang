'''
Created on 3 Jun 2014

@author: tpalys
'''

class Scene(object):

    def __init__(self, width, height, backgroundColor):
        self.width = width
        self.height = height
        self.children = []
        self.backgroundColor = backgroundColor


    def add(self, element):
        if element is list:
            for e in element:
                self.add(e)
        else:
            self.children.append(element)

    def extend(self, elements):
        for e in elements:
            self.add(e)

    def __str__(self):
        s = "({0}, {1})\n".format(self.width, self.height)

        for x in self.children:
            s += str(x) + "\n"

        return s

class Color(object):

    def __init__(self, red, green, blue):
        self.red = red * 255
        self.green = green * 255
        self.blue = blue * 255

    def __str__(self):
        return "Color: {0} {1} {2}".format(self.red, self.green, self.blue)

class Primitive(object):
    pass

class Polygon(Primitive):
    pass

class Rectangle(Polygon):

    def __init__(self, left, right, bottom, top, angle):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.angle = angle

    def __str__(self):
        return "Rectangle: {0} {1} {2} {3} {4}".format(self.left, self.top, self.right, self.bottom, self.angle)

class Circle(Primitive):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return "Circle: {0} {1} {2}".format(self.x, self.y, self.radius)

class Oval(Primitive):

    def __init__(self, x, y, a, b, angle):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.angle = angle

    def __str__(self):
        return "Oval: {0} {1} {2} {3} rotatedBy={4}".format(self.x, self.y, self.a, self.b, self.angle)

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

class Scale(Transformation):

    def __init__(self,ratio,ratio2):
        self.ratio = ratio
        self.ratio2 = ratio2

    def __str__(self):
        return "Scale: {0} {1}".format(self.ratio, self.ratio2)
