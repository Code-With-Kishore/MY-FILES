# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 05:55:48 2025

@author: Admin
"""

class A2nos():
    _x=None
    _y=None
    
    def __init__(self, a=10, b=20):
        self._x=a
        self._y=b
    def setx(self, a):
        self._x=a
    def sety(self, b):
        self._y=b
    def setxy(self, a, b):
        self._x=a
        self._y=b
    def reset(self):
        self._x=50
        self._y=50
    def setobject(self, a):
        self._x=a._x
        self._y=a._y
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getxy(self):
        return self._x, self._y
    def getobject(self):
        return self
    def display(self):
        print(self._x, self._y)
        
#main
c=A2nos()
c.display()

c.setx(500)
c.display()

c.sety(100)
c.display()
 
c.setxy(100, 200)
c.display()

c.reset()
c.display()

d=A2nos()
c.setobject(d)

a=c.getx()
b=c.gety()
e=c.getxy()
print(a)
print(b)
print(e)

y=c.getobject()
y.display()