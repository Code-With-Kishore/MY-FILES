# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 01:08:30 2025

@author: Admin
"""
from pgm437 import Op2nos
class Addition(Op2nos):
    def find(self):
        self._z = self._x + self._y  

# Main
x = Addition()
x.set()  
x.find()  
x.display()  
