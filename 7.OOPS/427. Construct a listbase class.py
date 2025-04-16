# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 05:31:31 2025

@author: Admin
"""

import random
class my_list():
    x=[]
    def __init__(self, n=10):
        self._x=[random.randint(0,100)for i in range(n)]
    def __str__(self):
        return ', '.join(map(str, self._x))
    def display(self):
        for i in self._x:
            print(i)

#main
l=my_list()
l.display()
print(l)        