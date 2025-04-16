# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:12:44 2024

@author: Admin
"""

from functools import reduce
n=int(input('Enter the tyms:'))
x=[int(input('Enter the value:'))for i in range(n)]
def sum(a,b):
    c=a+b
    return c
#main
y=reduce(sum,x)
print(y)