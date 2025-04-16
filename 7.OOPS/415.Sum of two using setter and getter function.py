# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 06:20:10 2024

@author: Admin
"""

class s2no():
    __x=None
    __y=None
    __s=None
    
    def __init__(self, a=10, b=20):
        self.__x=a
        self.__y=b
    def setx(self, a):
        self.__x=a
    def sety(self, b):
        self.__y=b
    def setxy(self, a, b):
        self.__x=a
        self.__y=b
    def reset(self):
        self.__x=50
        self.__y=50
    def setobject(self, a):
        self.__x=a.__x
        self.__y=a.__y
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getxy(self):
        return self.__x, self.__y
    def getobject(self):
        return self
    def find(self):
        self.__s=self.__x+self.__y
    def display(self):
        print(self.__s)
        
#main
c=s2no()
c.find()
c.display()

c.setx(500)
c.find()
c.display()

c.sety(100)
c.find()
c.display()
 
c.setxy(100, 200)
c.find()
c.display()

c.reset()
c.find()
c.display()

d=s2no()
c.setobject(d)

a=c.getx()
b=c.gety()
d=c.getxy()
print(a)
print(b)
print(d)

y=c.getobject()
y.find()
y.display()



