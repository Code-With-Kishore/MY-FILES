# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 05:22:45 2024

@author: Admin
"""

class sum_of_two():
    __x=None
    __y=None
    __z=None
    
    def set(self):
        self.__x=10
        self.__y=20    
        
    def find(self):
            self.__z = self.__x+self.__y
        
    def display(self):
                print(self.__z)
        
#main
a=sum_of_two()
a.set()
a.find()
a.display() 
