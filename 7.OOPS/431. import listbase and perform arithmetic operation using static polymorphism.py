# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 05:52:31 2025

@author: Admin
"""

from pgm427 import my_list

class ListscalOpr(my_list):
    def __add__(self, v): 
        return [i + v for i in self._x]

    def __sub__(self, v):  
        return [i - v for i in self._x]

    def __mul__(self, v):  
        return [i * v for i in self._x]

    def __truediv__(self, v):  
        return [i / v for i in self._x]

    def __floordiv__(self, v):  
        return [i // v for i in self._x]

    def __mod__(self, v):  
        return [i % v for i in self._x]

# Main
z = ListscalOpr()
z.display()

summ = z + 5
print("Addition:", summ)

diff = z - 5
print("Subtraction:", diff)

mul = z * 5
print("Multiplication:", mul)

t_div = z / 5
print("True Division:", t_div)

f_div = z // 5
print("Floor Division:", f_div)

modulus = z % 5
print("Modulus:", modulus)
