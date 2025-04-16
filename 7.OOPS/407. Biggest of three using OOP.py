# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 05:36:03 2024

@author: Admin
"""

class bot():
    __x=None
    __y=None
    __z=None
    __b=None
    
    def set(self):
        self.__x=100
        self.__y=500
        self.__z=1000
    def find(self):
        self.__b= (self.__x if self.__x>self.__z else self.__z) if self.__x>self.__y else (self.__y if self.__y>self.__z else self.__z)
    def display(self):
        print('Biggest value is:',self.__b)
    
#main
a=bot()
a.set()
a.find()
a.display()
