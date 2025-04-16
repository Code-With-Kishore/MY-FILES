# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 22:14:06 2024

@author: Admin
"""
#find the biggest and smallest of index.
a=[]
n=5
i=0
while i<n:
    b=int(input('Enter the b value:'))
    a.append(b)
    i=i+1
  
ln=len(a)
b=0
s=999
c=d=0
i=0
while i<=ln-1:
   if a[i]>=b:
       b=a[i]
       c=i
   elif a[i]<=s:
       s=a[i]
       d=i
   else:
       pass
   i=i+1
print(c)
print(d)