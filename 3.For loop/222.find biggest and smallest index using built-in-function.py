# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:15:37 2024

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

print('maximum index is:',max_index)
print('minimum index is:',min_index)