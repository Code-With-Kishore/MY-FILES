# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 06:57:49 2024

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
    