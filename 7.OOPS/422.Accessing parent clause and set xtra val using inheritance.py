# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:53:04 2024

@author: Admin
"""

from pgm417 import A2nos

class A3nos(A2nos):
    __z = None

    def __init__(self, a=10, b=20, c=30):
        super().__init__(a, b)
        self.__z = c

    def setz(self, c):
        self.__z = c

    def setxyz(self, a, b, c):
        self.setx(a)
        self.sety(b)
        self.__z = c

    def reset(self):
        super().reset()
        self.__z = 15

    def setobject(self, d):
        super().setobject(d)
        self.__z = d.__z  

    def getz(self):
        return self.__z

    def getxyz(self):
        return self.getx(), self.gety(), self.__z  

    def getobject(self):
        return self

    def display(self):
        super().display()
        print(self.__z)


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

a = c.getx()
b = c.gety()
z = c.getz()
xyz = c.getxyz()
print(a)
print(b)
print(xyz)
print(z)
