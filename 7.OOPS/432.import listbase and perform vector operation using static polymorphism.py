# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 06:27:03 2025

@author: Admin
"""

from pgm427 import my_list  
import random 

class ScalarOperations(my_list): 
    def __add__(self, otherlist):
        return [self._x[i] + otherlist[i] for i in range(len(self._x))]

    def __sub__(self, otherlist):  
        return [self._x[i] - otherlist[i] for i in range(len(self._x))]

    def __mul__(self, otherlist):  
        return [self._x[i] * otherlist[i] for i in range(len(self._x))]

    def __truediv__(self, otherlist):  
        return [self._x[i] / otherlist[i] for i in range(len(self._x))]

    def __floordiv__(self, otherlist):  
        return [self._x[i] // otherlist[i] for i in range(len(self._x))]

    def __mod__(self, otherlist):  
        return [self._x[i] % otherlist[i] for i in range(len(self._x))]

# Main
z = ScalarOperations()
z.display()


otherlist = [random.randint(1, 100) for i in range(10)]
print("Other list:", otherlist)


s = z + otherlist
print("Addition:", s)

d = z - otherlist
print("Subtraction:", d)

p = z * otherlist
print("Multiplication:", p)

td = z / otherlist
print("True Division:", td)

fd = z // otherlist
print("Floor Division:", fd)

m = z % otherlist
print("Modulus:", m)
