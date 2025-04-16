# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:36:31 2024

@author: Admin
"""

class s2no():
    __x=None
    __y=None
    __s=None
    
    def __init__(self):
        self.__x=10
        self.__y=20
    def find(self):
        self.__s=self.__x+self.__y
    def display(self):
        print('Sum of two:',self.__s)
        
#main
a=s2no()
a.find()
a.display()
