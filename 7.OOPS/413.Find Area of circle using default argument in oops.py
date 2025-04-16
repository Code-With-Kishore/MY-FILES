# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 05:37:10 2024

@author: Admin
"""

class aoc():
    __a=None
    __c=None
    
    def __init__(self, a=10):
        self.__a=a
    def find(self):
        self.__c=22/7*self.__a*self.__a
    def display(self):
        print('Area of circle:',self.__c)
        
#main
a=aoc()
a.find()
a.display()

b=aoc(100)
b.find()
b.display()

