# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 06:03:22 2025

@author: Admin
"""


from pgm438 import Opnos 

class SumImplementation(Opnos):  
    def Set(self, a, b):  
        self._a = a
        self._b = b

    def find(self):  
        self.result = self._a + self._b

    def display(self):  
        print("Sum of two numbers:", self.result)


# Main 
obj = SumImplementation()  
obj.Set(5, 5)  
obj.find()  
obj.display()  

    
        
