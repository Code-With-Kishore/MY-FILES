# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 07:12:38 2024

@author: Admin
"""

a=set()
n=int(input('Enter n value:'))
for i in range(n):
    x=int(input('Enter append value:'))
    a.add(x)
sum=0
for z in a:
    sum+=z
print('Sum of the element in set:', sum)