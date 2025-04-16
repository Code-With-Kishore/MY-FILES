# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 05:36:08 2024

@author: Admin
"""

class s2no():
    __x=None
    __y=None
    __s=None
    
    def __init__(self, x=10, y=20):
        self.__x=x
        self.__y=y
    def find(self):
        self.__s=self.__x+self.__y
    def display(self):
        print('Sum of two:',self.__s)
        
#main
a=s2no()
a.find()
a.display()

b=s2no(100)
b.find()
b.display()

c=s2no(100, 200)
c.find()
c.display()

    