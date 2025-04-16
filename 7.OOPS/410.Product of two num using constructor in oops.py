# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:42:34 2024

@author: Admin
"""

class s2no():
    __x=None
    __y=None
    __p=None
    
    def __init__(self):
        self.__x=10
        self.__y=20
    def find(self):
        self.__p = self.__x * self.__y
    def display(self):
        print('Product of two:',self.__p)
        
#main
a=s2no()
a.find()
a.display()
