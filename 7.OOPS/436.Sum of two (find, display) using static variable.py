# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:29:05 2025

@author: Admin
"""

class xyz():
    var=0
    _x=None
    _y=None
    _z=None
    def __init__(self,a=10,b=20):
        self._x=a
        self._y=b
        xyz.var+=1
    def find(self):
        self._z=self._x+self._y
    def displaly(self):
        print(self._z)
        
#main
f=xyz()
f.find()
f.displaly()

g=xyz(a=100)
g.find()
g.displaly()

h=xyz(b=200)
h.find()
h.displaly()

print(xyz.var)

        