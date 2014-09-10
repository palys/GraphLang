'''
Created on 19 kwi 2014

@author: tpalys
'''

import src.scene.scene as scene

objects = {}

class Program(object):
    def __init__(self, objects_definitions, scene):
        self.objects_definitions = objects_definitions
        self.scene = scene

    def toScene(self):
        return self.scene.toScene()

    def __str__(self):
        return "Program: \n" + str(self.objects_definitions) + str(self.scene)


class ObjectsDefinitions(object):
    def __init__(self):
        self.definitions = []

    def append(self, definition):
        self.definitions.append(definition)

    def extend(self, definitions):
        self.definitions.extend(definitions)

    def __str__(self):
        s = "Objects definitions: \n"
        for x in self.definitions:
            s += str(x) + "\n"
        return s

class ObjectDefinition(object):
    def __init__(self, ID, body):
        self.ID = ID
        self.body = body
        objects[ID] = body

    def toScene(self):
        return self.body.toScene()

    def __str__(self):
        return "Object definition: " + self.ID + "\n" + str(self.body)


class ObjectBody(object):
    def __init__(self, default_color, rest):
        self.default_color = default_color
        self.rest = rest

    def toScene(self):
        s = [self.default_color.toScene()]
        s.extend(self.rest.toScene())
        return s

    def __str__(self):
        return "Object body: \n" + str(self.default_color) + str(self.rest)


class ColorDefinition(object):
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def toScene(self):
        return scene.Color(self.red, self.green, self.blue)

    def __str__(self):
        return "color: {0} {1} {2}\n".format(self.red, self.green, self.blue)

class ObjectBodyRest(object):
    def __init__(self):
        self.nodeList = []

    def append(self, objectNode):
        self.nodeList.append(objectNode)

    def extend(self, nodes):
        self.nodeList.extend(nodes)

    def reverse(self):
        self.nodeList.reverse()

    def toScene(self):
        s = []
        l = [x.toScene() for x in self.nodeList]

        for x in l:
            if type(x) is list:
                s.extend(x)
            else:
                s.append(x)

        return s

    def __str__(self):
        s = "Object body rest :"
        for x in self.nodeList:
            s += str(x) + "\n"
        return s

class TransformationNodes(object):
    def __init__(self):
        self.nodes = []

    def append(self, node):
        self.nodes.append(node)

    def extend(self, nodes):
        self.nodes.extend(nodes)

    def toScene(self):
        return [x.toScene() for x in self.nodes]

class Node(object):
    pass

class UsageNode(Node):
    def __init__(self, ID):
        self.ID = ID

    def toScene(self):
        s =  objects[self.ID].toScene()
        return s

    def __str__(self):
        return "Usage of " + self.ID + "\nBody is: \n" + str(objects[self.ID])

class TransformationNode(Node):
    pass

class Primitive(Node):
    pass

class Polygon(Primitive):
    pass

class Rectangle(Polygon):
    def __init__(self, left, top, right, bottom, angle=0):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.angle = angle

    def toScene(self):
        return scene.Rectangle(self.left, self.right, self.bottom, self.top, self.angle)

class Circle(Primitive):
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius

    def toScene(self):
        return scene.Circle(self.x, self.y, self.radius)

class Oval(Primitive):
    def __init__(self,x,y,a,b,angle=0):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.angle = angle

    def toScene(self):
        return scene.Oval(self.x, self.y, self.a, self.b, self.angle)

class Rotation(TransformationNode):
    def __init__(self, angle):
        self.angle = angle

    def toScene(self):
        return scene.Rotation(self.angle)

class Translation(TransformationNode):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def toScene(self):
        return scene.Translation(self.dx, self.dy)

class Scale(TransformationNode):
    def __init__(self, ratio, ratio2):
        self.ratio = ratio
        self.ratio2 = ratio2

    def toScene(self):
        return scene.Scale(self.ratio, self.ratio2)

class Scene(object):
    def __init__(self, width, height, body):
        self.width = width
        self.height = height
        self.body = body

    def toScene(self):
        s = scene.Scene(self.width, self.height)
        s.extend(self.body.toScene())
        return s

    def __str__(self):
        return "scene: {0} {1}\n".format(self.width, self.height) + str(self.body)
