# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:34:00 2024

@author: Admin
"""

a=[]
n=int(input('Enter n integer values:'))
for i in range(0,n):
    d=int(input('Enter the value: '))
    a.append(d)

x=max(a)
max_index=a.index(x)

y=min(a)
min_index=a.index(y)

a[max_index]=y
a[min_index]=x
print(a)

