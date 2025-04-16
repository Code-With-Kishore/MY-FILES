# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 07:08:17 2025

@author: Admin
"""


from pgm438 import Opnos  

class bot(Opnos):  
    
    _x = None
    _y = None
    _z = None
    _b = None  
    
    def Set(self, x=100, y=200, z=300):
        self._x = x
        self._y = y
        self._z = z
        
    def find(self):
        self._b = (self._x if self._x > self._z else self._z) if self._x > self._y else (self._y if self._y > self._z else self._z)
        
    def display(self):
        print('Biggest value is:', self._b)  
        
# Main
obj = bot()  
obj.Set(10, 15, 20)  
obj.find()  
obj.display()

    