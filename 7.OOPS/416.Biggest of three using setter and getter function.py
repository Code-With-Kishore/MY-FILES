# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 09:06:20 2024

@author: Admin
"""

class bot():
    __x=None
    __y=None
    __z=None
    __big=None
    
    def __init__(self, a=10, b=20, c=30):
        self.__x=a
        self.__y=b
        self.__z=c
    def setx(self, a):
        self.__x=a
    def sety(self, b):
        self.__y=b
    def setz(self, c):
        self.__z=c
    def setxyz(self, a, b, c):
        self.__x=a
        self.__y=b
        self.__z=c
    def reset(self):
        self.__x=500
        self.__y=1000
        self.__z=1500
    def setobject(self, a):
        self.__x=a.__x
        self.__y=a.__y
        self.__z=a.__z
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getz(self):
        return self.__z
    def getxyz(self):
        return self.__x, self.__y, self.__z
    def getobject(self):
        return self
    def find(self):
        self.__big=(self.__x if self.__x>self.__z else self.__z) if self.__x>self.__y else (self.__y if self.__y>self.__z else self.__z)
    def display(self):
        print(self.__big)
        
#main
c=bot()
c.find()
c.display()

c.setx(50)
c.find()
c.display()

c.sety(60)
c.find()
c.display()

c.setz(70)
c.find()
c.display()
 
c.setxyz(10, 20, 30)
c.find()
c.display()

c.reset()
c.find()
c.display()

d=bot()
c.setobject(d)

a=c.getx()
b=c.gety()
e=c.getz()
d=c.getxyz()
print(a)
print(b)
print(d)
print(e)

y=c.getobject()
y.find()
y.display()
