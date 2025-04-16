# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 07:07:02 2024

@author: Admin
"""

#sum of the element of each row.
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
    
i=0
while i<rows:
    x=0
    j=0
    while j<cols:
        x=x+m[i][j]
        j=j+1
    print(x)
    i=i+1
    