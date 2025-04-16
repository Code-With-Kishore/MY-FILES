# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:39:33 2025

@author: Admin
"""

from pgm427 import my_list  
import random 

class ScalarOperations(my_list):
    def __init__(self, x=10):
        super().__init__(x)  
    
    def add(self, otherlist):
        return [self._x[i] + otherlist[i] for i in range(len(self._x))]

    def subtract(self, otherlist):
        return [self._x[i] - otherlist[i] for i in range(len(self._x))]

    def multiply(self, otherlist):
        return [self._x[i] * otherlist[i] for i in range(len(self._x))]

    def divide(self, otherlist):
        
        return [ self._x[i] / otherlist[i] for i in range(len(self._x)) ]

    def floordiv(self, otherlist):
        
        return [self._x[i] // otherlist[i] for i in range(len(self._x))]

    def mod(self, otherlist):
        
        return [self._x[i] % otherlist[i] for i in range(len(self._x)) ]

# main
z = ScalarOperations()
z.display()  

otherlist = [random.randint(1,100)for i in range(10)]
print("Other list:", otherlist)

s = z.add(otherlist)
print("Addition:", s)

d = z.subtract(otherlist)
print("Subtraction:", d)

p = z.multiply(otherlist)
print("Multiplication:", p)

td = z.divide(otherlist)
print("True Division:", td)

fd = z.floordiv(otherlist)
print("Floor Division:", fd)

m = z.mod(otherlist)
print("Mod:", m)
