# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 07:17:34 2024

@author: Admin
"""

a=set()
n=int(input('Enter n value:'))
for i in range(n):
    x=int(input('Enter append value:'))
    a.add(x)
print(a)

b=0
for z in a:
    b=z if z>b else b
print('biggest element of set is:', b)

    