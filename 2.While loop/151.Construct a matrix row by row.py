# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 01:07:36 2024

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
    
ln=len(m)
i=0
while i<=ln-1:
    print(m[i])
    i=i+1

