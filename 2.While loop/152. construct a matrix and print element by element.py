# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 06:36:17 2024

@author: Admin
"""

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
    j=0
    while j<cols:
        print(m[i][j])
        j=j+1
    i=i+1
    