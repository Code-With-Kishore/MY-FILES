# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 06:14:25 2024

@author: Admin
"""

class s2no():
    __x=None
    __y=None
    __s=None
    
    def set(self):
        self.__x=50
        self.__y=50
    def find(self):
        self.__s=self.__x+self.__y
    def display(self):
        print(self.__s)
        
#main
a=s2no()
a.set()
a.find()
a.display()

b=s2no()
b.set()
b.find()
b.display()

c=s2no()
c.set()
c.find()
c.display()
