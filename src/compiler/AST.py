'''
Created on 19 kwi 2014

@author: tpalys
'''

import src.scene.shape2d.primitives.Rectangle as Rec
from src.scene.shape2d.nodes.transformation import RotationNode, TranslationNode
import src.scene.shape2d.nodes.add.OrNode as OrNode
import src.scene.shape2d.nodes.ColorNode as ColorNode
from src.scene.shape2d.OperationList2D import OperationList2D
import src.scene.Scene as SScene

objects = {}

class Program(object):
    def __init__(self, objects_definitions, scene):
        self.objects_definitions = objects_definitions
        self.scene = scene

    def toScene(self):
        print "Program.toScene"
        return self.scene.toScene()


class ObjectsDefinitions(object):
    def __init__(self):
        self.definitions = []

    def append(self, definition):
        self.definitions.append(definition)

    def extend(self, definitions):
        self.definitions.extend(definitions)

class ObjectDefinition(object):
    def __init__(self, ID, body):
        self.ID = ID
        self.body = body
        objects[ID] = self

    def toScene(self):
        print "ObjectDefinition.toScene"
        return self.body.toScene()


class ObjectBody(object):
    def __init__(self, default_color, rest):
        self.default_color = default_color
        self.rest = rest

    def toScene(self):
        print "ObjectBody.toScene"
        operations = OperationList2D([self.default_color.toScene()])
        operations.addChildren(self.rest.toScene())
        return operations


class ColorDefinition(object):
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def toScene(self):
        print "ColorDefinition.toScene"
        return ColorNode.ColorNode(self.red, self.green, self.blue)

class ObjectBodyRest(object):
    def __init__(self):
        self.nodeList = []

    def append(self, objectNode):
        self.nodeList.append(objectNode)

    def extend(self, nodes):
        self.nodeList.extend(nodes)

    def toScene(self):
        print "ObjectBodyRest.toScene"
        return [x.toScene() for x in self.nodeList]

class TransformationNodes(object):
    def __init__(self):
        self.nodes = []

    def append(self, node):
        self.nodes.append(node)

    def extend(self, nodes):
        self.nodes.extend(nodes)

    def toScene(self):
        print "TransformationNodes.toScene"
        return [x.toScene() for x in self.nodes]

class Node(object):
    pass

class UsageNode(Node):
    def __init__(self, ID):
        self.ID = ID

    def toScene(self):
        print "UsageNode.toScene"
        s =  objects[self.ID].toScene()
        print "UsageNode.toScene ----- END"
        return s

class TransformationNode(Node):
    pass

class Primitive(Node):
    pass

class Rectangle(Primitive):
    def __init__(self, left, top, right, bottom):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def toScene(self):
        print "Rectangle.toScene"
        rec =  Rec.Rectangle(self.right - self.left, self.bottom - self.top, self.left, self.right)
        return OrNode.OrNode(rec)

class Rotation(TransformationNode):
    def __init__(self, angle):
        self.angle = angle

    def toScene(self):
        print "Rotation.toScene"
        return RotationNode.RotationNode(self.angle)

class Translation(TransformationNode):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def toScene(self):
        print "Translation.toScene"
        return TranslationNode.TranslationNode(self.dx, self.dy)

class Scene(object):
    def __init__(self, width, height, body):
        self.width = width
        self.height = height
        self.body = body

    def toScene(self):
        print "Scene.toScene"
        s = SScene.Scene(self.width, self.height)
        for x in self.body.toScene():
            s.addComponent(x)
        print "Scene.toScene ---------- END"
        return s
