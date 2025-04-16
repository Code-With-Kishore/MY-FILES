# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 00:21:20 2024

@author: Admin
"""

a=[]
n=5
i=0
while i<n:
    b=int(input('Enter the b value:'))
    a.append(b)
    i=i+1
  
ln=len(a)
b=0
i=0
while i<=ln-1:
   if a[i]>=b:
       b=a[i]
       c=i
       i=i+1
print(c)