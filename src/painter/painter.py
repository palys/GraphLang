import Tkinter
import math, cmath
from src.scene.scene import *

def addToClass(cls):
    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class Painter():
    def __init__(self,s):
        self.scene = s
        self.color = Color(0,0,0)
        self.top = Tkinter.Tk()
        self.C = Tkinter.Canvas(self.top, bg=self.rgb_to_string(self.scene.backgroundColor), height=s.height, width=s.width)

    def paintScene(self):
        map(lambda x: x.addToCanvas(self), self.scene.children)

        self.C.pack()
        self.top.mainloop()

    def change_color(self,color):
        self.color = color

    def rgb_to_string(self, color):
        rgb = color.red, color.green, color.blue
        return '#%02x%02x%02x' % rgb

    @addToClass(Color)
    def addToCanvas(self, painter):
        painter.change_color(self)

    @addToClass(Rectangle)
    def addToCanvas(self, painter):
        params = self.left,self.top,self.right,self.bottom
        color = painter.rgb_to_string(painter.color)
        if self.angle != 0:
            params = painter.rect_to_poly(params)
            params = painter.rotate_polygon(params, self.angle)
            return painter.C.create_polygon(params, fill=color, outline=color, tags="tag")
        else:
            return painter.C.create_rectangle(params, fill=color, outline=color, tags="tag")

    @addToClass(Circle)
    def addToCanvas(self, painter):
        r = self.radius
        params = self.x - r, self.y - r, self.x + r, self.y + r
        color = painter.rgb_to_string(painter.color)
        return painter.C.create_oval(params, fill=color, outline=color, tag="tag")

    @addToClass(Oval)
    def addToCanvas(self, painter):
        params = self.x - self.a, self.y - self.b, self.x + self.a, self.y + self.b
        color = painter.rgb_to_string(painter.color)
        if self.angle != 0:
            return painter.C.create_polygon(painter.oval_to_poly(params[0],params[1],params[2],params[3], rotation=self.angle), fill=color, outline=color, tag="tag")
        else:
            return painter.C.create_oval(params, fill=color, outline=color, tag="tag")


    @addToClass(Rotation)
    def addToCanvas(self, painter):
        print "rotation"

    @addToClass(Translation)
    def addToCanvas(self, painter):
        return painter.C.move("tag",self.dx, self.dy)

    @addToClass(Scale)
    def addToCanvas(self,painter):
        return painter.C.scale("tag",painter.scene.width/2,painter.scene.height/2,self.ratio, self.ratio2)

    def rect_to_poly(self, params):
        l = params[0]
        t = params[1]
        r = params[2]
        b = params[3]
        newxy = [(l,t),(l,b),(r,b),(r,t)]
        return newxy

    def rotate_polygon(self, params, angle):
        cangle = cmath.exp(angle*1j*math.pi/180)

        offset = complex(params[0][0], params[0][1])
        newxy = []
        for x, y in params:
            v = cangle * (complex(x, y) - offset) + offset
            newxy.append(v.real)
            newxy.append(v.imag)
        return newxy

    def oval_to_poly(self,x0,y0, x1,y1, steps=100, rotation=0):
        # x0,y0,x1,y1 are as create_oval

        # rotation is in degrees anti-clockwise, convert to radians
        rotation = rotation * math.pi / 180.0

        # major and minor axes
        a = (x1 - x0) / 2.0
        b = (y1 - y0) / 2.0

        # center
        xc = x0 + a
        yc = y0 + b

        point_list = []

        # create the oval as a list of points
        for i in range(steps):

            # Calculate the angle for this step
            # 360 degrees == 2 pi radians
            theta = (math.pi * 2) * (float(i) / steps)

            x1 = a * math.cos(theta)
            y1 = b * math.sin(theta)

            # rotate x, y
            x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
            y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

            point_list.append(round(x + xc))
            point_list.append(round(y + yc))

        return point_list