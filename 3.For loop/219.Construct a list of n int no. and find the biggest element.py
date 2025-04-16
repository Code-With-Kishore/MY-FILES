# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:23:09 2024

@author: Admin
"""

a=[]
n=int(input('Enter n integer values:'))
for i in range(0,n):
    d=int(input('Enter the value: '))
    a.append(d)
print(a)
    
b=0
for j in a:
    c=j if j>b else b
print(c)