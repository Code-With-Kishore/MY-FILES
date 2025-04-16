# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 05:46:32 2024

@author: Admin
"""
a=[]
n=int(input('Enter n integer values:'))
for i in range(0,n):
    d=int(input('Enter the value: '))
    a.append(d)

biggest=max(a)
biggest_index=a.index(biggest)

smallest=min(a)
smallest_index=a.index(smallest)

sec_big=0
sec_big_index=a[0]
for i in range(len(a)):
    if i!=biggest_index:
        if a[i]>sec_big:
            sec_big=a[i]
            sec_big_index=i

print('second biggest index value is:', sec_big_index)

sec_small=0
sec_small_index=a[0]

for i in range(len(a)):
    if i!=smallest_index:
        if a[i]<sec_small:
            sec_small=a[i]
            sec_small_index=i

print('second smallest index value is:', sec_small_index )            

a[sec_big_index]=sec_small
a[sec_small_index]=sec_big

print(a)