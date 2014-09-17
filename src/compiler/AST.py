'''
Created on 19 kwi 2014

@author: tpalys
'''

import src.scene.scene as scene

objects = {}

class Global(object):
    def __init__(self):
        self.variables = {}

currentBlock = Global()


class Program(object):
    def __init__(self, objects_definitions, scene):
        self.objects_definitions = objects_definitions
        self.scene = scene
        self.variables = {}

    def toScene(self):
        currentBlock = self
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

    def insert(self, index, node):
        self.nodes.insert(index, node)

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
    def __init__(self, width, height, body, declarations):
        self.width = width
        self.height = height
        self.body = body
        self.variables = {}
        self.declarations = declarations

    def toScene(self):
        s = scene.Scene(self.width, self.height)
        currentBlock = self
        self.declarations.toScene()
        s.extend(self.body.toScene())
        return s

    def __str__(self):
        return "scene: {0} {1}\n".format(self.width, self.height) + "[" + str(self.declarations) + "]\n" + str(self.body)

class Declarations(object):
    def __init__(self):
        self.declarations = []

    def toScene(self):
        for dec in self.declarations:
            dec.toScene()

    def append(self, declaration):
        self.declarations.append(declaration)

    def extend(self, declarations):
        self.declarations.append(declarations)

    def insert(self, declaration):
        self.declarations.insert(0, declaration)

    def __str__(self):
        s = "declarations:\n"
        for dec in self.declarations:
            s += str(dec) + "\n"
        return s

class Type(object):

    instances = {}
    initialized = False

    @staticmethod
    def initialize():
        Type.initialized = True
        Type.instances = {"integer" : Type("integer"), "float" : Type("float")}

    def __init__(self, value):
        if not Type.initialized:
            Type.initialize()
        self.value = value

    def toScene(self):
        print "TODO"

    def __str__(self):
        return str(self.value)

    @staticmethod
    def ofInt():
        if not Type.initialized:
            Type.initialize()
        return Type.instances["integer"]

    @staticmethod
    def ofFloat():
        if not Type.initialized:
            Type.initialize()
        return Type.instances["float"]

    def eq(self, other):
        return self.value == other.value

class Declaration(object):
    def __init__(self, dec_type, declarators):
        self.declaration_type = dec_type
        self.declarators = declarators

    def toScene(self):
        self.declarators.toScene(self.declaration_type)

    def __str__(self):
        return "declaration ({0}, {1})".format(self.declaration_type, self.declarators)

class Declarators(object):
    def __init__(self, declarator):
        self.dec = []
        self.dec.append(declarator)

    def toScene(self, dec_type):
        map(lambda x : x.toScene2(dec_type), self.dec)

    def append(self, declarator):
        self.dec.append(declarator)

    def insert(self, declarator):
        self.dec.insert(0, declarator)

    def __str__(self):
        s = "declarators: ("
        for d in self.dec:
            s += str(d) + " "
        s += ")"
        return s

class Expression(object):

    @staticmethod
    def ofConst(constant):
        e = Expression(0)
        e.constant = constant
        return e

    @staticmethod
    def ofID(id):
        e = Expression(1)
        e.id = id
        return e

    @staticmethod
    def ofTwoArg(e1, op, e2):
        e = Expression(2)
        e.e1 = e1
        e.e2 = e2
        e.op = Operator(op)
        return e

    def __init__(self, t):
        self.t = t

    def toScene(self):
        print "TODO"

    def __str__(self):
        return str(self.getValue())

    def getType(self):
        if self.t == 0:
            if type(self.constant) is int:
                return Type.ofInt()
            elif type(self.constant) is float:
                return Type.ofFloat()
        elif self.t == 1:
            return currentBlock.variables[self.id].getType()
        elif self.t == 2:
            return self.op.getType(self.e1, self.e2)

    def getValue(self):
        if self.t == 0:
            return self.constant
        elif self.t == 1:
            return currentBlock.variables[self.id].getValue()
        elif self.t == 2:
            return self.op.compute(self.e1, self.e2)

class Operator():

    initialized = False
    result = {}
    operation = {}

    @staticmethod
    def initialize():

        Operator.result["+"] = {}
        Operator.result["+"][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofFloat()}
        Operator.result["+"][Type.ofFloat()] = {Type.ofInt() : Type.ofFloat(), Type.ofFloat() : Type.ofFloat()}

        Operator.result["-"] = {}
        Operator.result["-"][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofFloat()}
        Operator.result["-"][Type.ofFloat()] = {Type.ofInt() : Type.ofFloat(), Type.ofFloat() : Type.ofFloat()}


        Operator.result["*"] = {}
        Operator.result["*"][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofFloat()}
        Operator.result["*"][Type.ofFloat()] = {Type.ofInt() : Type.ofFloat(), Type.ofFloat() : Type.ofFloat()}


        Operator.result["/"] = {}
        Operator.result["/"][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofFloat()}
        Operator.result["/"][Type.ofFloat()] = {Type.ofInt() : Type.ofFloat(), Type.ofFloat() : Type.ofFloat()}


        Operator.result["<"] = {}
        Operator.result["<"][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}
        Operator.result["<"][Type.ofFloat()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}


        Operator.result["<="] = {}
        Operator.result["<="][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}
        Operator.result["<="][Type.ofFloat()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}

        Operator.result[">"] = {}
        Operator.result[">"][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}
        Operator.result[">"][Type.ofFloat()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}

        Operator.result[">="] = {}
        Operator.result[">="][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}
        Operator.result[">="][Type.ofFloat()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}

        Operator.result["=="] = {}
        Operator.result["=="][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}
        Operator.result["=="][Type.ofFloat()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}

        Operator.result["!="] = {}
        Operator.result["!="][Type.ofInt()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}
        Operator.result["!="][Type.ofFloat()] = {Type.ofInt() : Type.ofInt(), Type.ofFloat() : Type.ofInt()}


        Operator.operation["+"] = lambda x,y : x + y
        Operator.operation["-"] = lambda x,y : x - y
        Operator.operation["/"] = lambda x,y : x / y
        Operator.operation["*"] = lambda x,y : x * y
        Operator.operation[">"] = lambda x,y : 1 if x > y else 0
        Operator.operation[">="] = lambda x,y : 1 if x >= y else 0
        Operator.operation["<"] = lambda x,y : 1 if x < y else 0
        Operator.operation["<="] = lambda x,y : 1 if x <= y else 0
        Operator.operation["=="] = lambda x,y : 1 if x == y else 0
        Operator.operation["!="] = lambda x,y : 1 if x != y else 0

        Operator.initialized = True

    def __init__(self, op):
        if not Operator.initialized:
            Operator.initialize()
        self.op = op

    @staticmethod
    def ofAddition():
        return Operator("+")

    @staticmethod
    def ofSubtraction():
        return Operator("-")

    @staticmethod
    def ofMultiplication():
        return Operator("*")

    @staticmethod
    def ofDivision():
        return Operator("/")


    def getType(self, arg1, arg2):
        print "About to get type " + str(self.op) + " " + str(arg1.getType()) + " " + str(arg2.getType())
        print str(Operator.result[self.op])
        print str(Operator.result[self.op][arg1.getType()])


        return Operator.result[self.op][arg1.getType()][arg2.getType()]

    def compute(self, arg1, arg2):
        return Operator.operation[self.op](arg1.getValue(), arg2.getValue())

class Declarator(object): # TODO check
    def __init__(self, name):
        self.name = name
        self.hasValueSet = False
        self.value = None

    def setExpr(self, value):
        self.value = value
        self.hasValueSet = True

    def getExpr(self):
        if self.hasValueSet:
            return self.value
        raise ValueError("Variable has no expr set")

    def toScene(self):
        t = currentBlock.variables[self.name].getType()
        if not t.eq(self.value.getType()):
            raise "Incorrect assignment"
        else:
            currentBlock.variables[self.name].setValue(self.value.getValue())

    def toScene2(self, declarationType):

        print "try to add " + self.name

        if self.name in currentBlock.variables:
            raise ValueError("{0} declared twice in one scope.")
        elif self.hasValueSet:
            if self.value.getType().eq(declarationType):
                print "Added to scope " + self.name
                currentBlock.variables[self.name] = ValueHolder(declarationType)
                currentBlock.variables[self.name].setValue(self.value.getValue())
            else:
                raise ValueError("Wrong type of {0}").format(self.name)
        else:
            print "Added to scope " + self.name
            currentBlock.variables[self.name] = ValueHolder(declarationType)

    def __str__(self):
        return "declarator ({0}, {1})".format(self.name, self.value)

class ValueHolder(object):
    def __init__(self, variableType):
        self.hasValueSet = False
        self.t = variableType

    def setValue(self, value):
        self.value = value
        self.hasValueSet = True

    def getValue(self):
        if self.hasValueSet:
            return self.value
        raise ValueError("Value not set")

    def getType(self):
        return self.t

    def erase(self):
        self.hasValueSet = False

    def __str__(self):
        return str(self.value)

class IfExpr(object):
    def __init__(self, condition, trueBody):
        self.condition = condition
        self.trueBody = trueBody
        self.hasElse = False

    @staticmethod
    def ofOnlyTrue(condition, trueBody):
        return IfExpr(condition, trueBody)

    @staticmethod
    def ofTrueFalse(condition, trueBody, elseBody):
        iff = IfExpr(condition, trueBody)
        iff.elseBody = elseBody
        iff.hasElse = True
        return iff

    def toScene(self):
        if self.condition.getValue() == 1:
            return self.trueBody.toScene()
        elif self.hasElse:
            return self.elseBody.toScene()

class WhileExpr(object):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def toScene(self):
        result = []
        while self.condition.getValue() == 1:
            result.append(self.body.toScene())
        return result

class Blocks(object):
    def __init__(self):
        self.children = []

    def append(self, child):
        self.children.append(child)

    def toScene(self):
        s = []
        for c in self.children:
            ss = c.toScene()
            if type(ss) is list:
                s.extend(ss)
            elif ss is not None:
                s.append(ss)
        return s



















































