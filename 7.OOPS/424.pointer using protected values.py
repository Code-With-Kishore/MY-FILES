# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:22:01 2025

@author: Admin
"""

from pgm417 import A2nos

class point(A2nos):    
    def __init__(self, a=5, b=10):
        self._x=a
        self._y=b
    
    def move_right(self, dx):
        self._x= self._x+dx
    
    def move_left(self, dx):
        self._x= self._x-dx
        
    def move_up(self, dy):
        self._y= self._y+dy
        
    def move_down(self, dy):
        self._y=self._y-dy
        
    def move_random(self, dx, dy):
        self._x=self._x+dx
        self._y=self._y+dy
        
    def display(self):
        print(self._x, self._y)
        
# Main
c = point()
c.display()

c.move_right(10)
c.display()

c.move_left(20)
c.display()

c.move_up(30)
c.display()

c.move_down(40)
c.display()

c.move_random(50, 60)
c.display()