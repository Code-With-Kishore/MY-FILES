# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 04:51:54 2024

@author: Admin
"""

class aoc():
    __r=None
    __c=None
    def set(self):
        self.__r=40
    def find(self):
        self.__c=22/7*self.__r*self.__r
    def display(self):
        print(self.__c)
        
#main
a=aoc()
a.set()
a.find()
a.display()

        
        