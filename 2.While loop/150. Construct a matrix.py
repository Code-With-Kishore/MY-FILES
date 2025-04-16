# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 00:40:21 2024

@author: Admin
"""
#Construct a matrix.
m=[]

rows=3
cols=3
i=0
while i<rows:
    r=[]
    j=0
    while j<cols:
        a=int(input('Enter a value:'))
        r.append(a)
        j=j+1
    m.append(r)  
    i=i+1
print(m)
    
      