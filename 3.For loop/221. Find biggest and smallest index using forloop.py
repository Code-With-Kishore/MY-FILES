# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:46:21 2024

@author: Admin
"""

a=[]
n=int(input('Enter n integer values:'))
for i in range(0,n):
    d=int(input('Enter the value: '))
    a.append(d)


b=0
s=999
c=e=0
for i in range(0,len(a)):
    if a[i]>b:
        b=a[i]
        c=i
    elif a[i]<s:
        s=a[i]
        e=i
    else:
        pass
    
print('Biggest index is:',c)
print('Smallest index is:',e)


