from math import *

class Vector():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.xy = "(%.2f, %.2f)" % (self.x,self.y)
        self.mag = sqrt(self.x ** 2 + self.y ** 2)
        
        if isclose(x, 0):
            self.angle = 90.0
        else:
            self.angle = degrees(atan(abs(self.y) / abs(self.x)))
        if x < 0:
            self.angle = 180 - self.angle
        if y < 0:
            self.angle = 360 - self.angle

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)
    __rmul__ = __mul__
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
        
    def __repr__(self):
        return "(%.2f, %.2f) %.2f %.2f" % (self.x, self.y, self.mag, self.angle) + u'\xb0'

def toVect(x1,y1, x2,y2):
    return Vector(x2 - x1, y2 - y1)

def fromAngle(mag, angle):
    x = mag * cos(radians(angle))
    y = mag * sin(radians(angle))
    return Vector(x,y)

i = Vector(1,0)
j = Vector(0,1)

def tests():
    cases = [(0, 5, 90), (0, -5, 270), (5, 5, 45), (5, 0, 0), (-5, 0, 180),
    (5, -5, 315), (-5, -5, 225), (-5, 5, 135), (100, 1, 0.5729386976834859)]
    for x,y,a in cases:
        if not isclose(Vector(x,y).angle, a):
            raise Exception(f"FAIL Test ({x}, {y}): Expeced {a} but got {Vector(x,y).angle}")
    print(f"Ran {len(cases)} tests... OK")

if __name__ == "__main__":
    tests()
