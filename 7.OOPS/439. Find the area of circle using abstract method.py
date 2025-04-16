# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 06:55:46 2025

@author: Admin
"""

from pgm438 import Opnos 

class circle (Opnos):  
    _r=None
    _circle=None
    
    def Set(self,r):  
        self._r = r
       
    def find(self):  
        self._circle =22/7*self._r*self._r

    def display(self):  
        print("area of circle:", self._circle)


# Main 
obj = circle()  
obj.Set(10)  
obj.find()  
obj.display()  