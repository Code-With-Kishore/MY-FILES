# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:19:33 2024

@author: Admin
"""

a=[]
n=int(input('Enter n integer values:'))
for i in range(0,n):
    d=int(input('Enter the value: '))
    a.append(d)
print(a)

b=0
for i in a:
    b+=i
print(b)
