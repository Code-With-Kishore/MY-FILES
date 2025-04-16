# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:28:23 2024

@author: Admin
"""

a=[]
i=0
n=10
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
       i=i+1
       print(b)