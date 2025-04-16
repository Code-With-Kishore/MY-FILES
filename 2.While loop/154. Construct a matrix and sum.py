# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 06:42:44 2024

@author: Admin
"""

#Sum of the element of matrix.
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

x=0    
i=0
while i<rows:
    j=0
    while j<cols:
        x=x+m[i][j]
        j=j+1
    i=i+1
print(x)
    
        