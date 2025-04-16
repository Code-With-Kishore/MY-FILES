# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 06:09:55 2025

@author: Admin
"""

from pgm427 import my_list

class ScalarOperations(my_list):
    def __init__(self, x=10):
        super().__init__(x)

    def add(self, v):
        return [i + v for i in self._x]

    def subtract(self, v):
        return [i - v for i in self._x]

    def multiply(self, v):
        return [i * v for i in self._x]

    def divide(self, v):
       
        return [i / v for i in self._x]

    def floordiv(self, v):
        
        return [i // v for i in self._x]

    def mod(self, v):
        
        return [i % v for i in self._x]

# main

z = ScalarOperations()
z.display()


s=z.add(10)
print('Addition:',s)

d=z.subtract(5)
print('Subraction:',d)

p=z.multiply(5)
print('Multiplication',p)

td=z.divide(5)
print('True Division:',td)

fd=z.floordiv(5)
print('Floor Division:',fd)

m=z.mod(5)
print('Mod:',m)
