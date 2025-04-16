# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 06:05:43 2024

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

b=0
for j in d:
    if d[j]>b:
        b=d[j]
        c=j
    else:
        pass
s=999
for i in d:
    if d[i]<s:
        s=d[i]
        m=i
    else:
        pass
print(d)
print('highest occurance is:',c,b)
print('lowest occurance is:',m,s)