# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 05:48:55 2024

@author: Admin
"""

class bot():
    __x=None
    __y=None
    __z=None
    __b=None
    
    def __init__(self, i=100,j=200, k=300):
        self.__x=i
        self.__y=j
        self.__z=k
    def find(self):
        self.__b= (self.__x if self.__x>self.__z else self.__z) if self.__x>self.__y else (self.__y if self.__y>self.__z else self.__z)
    def display(self):
        print('Biggest value is:',self.__b)
    
#main
a=bot()
a.find()
a.display()

b=bot(1000)
b.find()
b.display()

c=bot(1000, 500)
c.find()
c.display()

d=bot(900, 500, 250)
d.find()
d.display()

