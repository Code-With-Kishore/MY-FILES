# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:44:59 2025

@author: Admin
"""

from pgm417 import A2nos

class A3nos(A2nos):
    _z = None

    def __init__(self, a=10, b=20, c=30):
        super().__init__(a, b)
        self._z = c

    def setz(self, c):
        self._z = c

    def setxyz(self, a, b, c):
        self._x=a
        self._y=b
        self._z = c

    def reset(self):
        super().reset()
        self._z = 15

    def setobject(self, d):
        super().setobject(d)
        self._z = d._z  

    def getz(self):
        return self._z

    def getxyz(self):
        return self.getx(), self.gety(), self._z  

    def getobject(self):
        return self

    def display(self):
        super().display()
        print(self._z)


# Main
c = A3nos()
c.display()

c.setz(100)
c.display()

c.setxyz(100, 200, 300)
c.display()

c.reset()
c.display()

d = A3nos()
c.setobject(d)

f = c.getobject()
f.display()


z = c.getz()
xyz = c.getxyz()

print(xyz)
print(z)
