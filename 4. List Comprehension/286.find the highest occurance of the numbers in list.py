# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 05:53:58 2024

@author: Admin
"""

import random
n=int(input('Enter n value:'))
a=[random.randint(0,1000)for i in range(n)]
x=set(a)

d={}
for i in x:
    y=a.count(i)
    d[i]=y
print(d)

b=0
for j in d:
    if d[j]>b:
        b=d[j]
        c=j
    else:
        pass
print(c,b)