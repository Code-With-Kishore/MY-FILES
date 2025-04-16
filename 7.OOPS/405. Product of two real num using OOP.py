# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 04:46:09 2024

@author: Admin
"""

class p2no():
    __x=None
    __y=None
    __p=None
    
    def set(self):
        self.__x=123.4
        self.__y=567.8
    def find(self):
        self.__p=self.__x*self.__y
    def display(self):
        print(self.__p)
        
#main
a=p2no()
a.set()
a.find()
a.display()
