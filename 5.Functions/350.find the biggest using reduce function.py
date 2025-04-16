# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:22:37 2024

@author: Admin
"""
from functools import reduce
n=int(input('Enter n value:'))
x=[int(input('Enter the value:'))for i in range(n)]
def big(a,b):
    c=a if a>b else b
    return c
#main
y=reduce(big,x)
print(y)
