# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 02:51:48 2024

@author: Admin
"""

a=[]
n=int(input('Enter n integer values:'))
for i in range(0,n):
    d=int(input('Enter the value: '))
    a.append(d)

biggest=max(a)
biggest_index=a.index(biggest)

sec_big=0

for i in range(len(a)):
    if i!=biggest_index:
        if a[i]>sec_big:
            sec_big=a[i]
            sec_big_index=i
        else:
            pass
print(sec_big_index)