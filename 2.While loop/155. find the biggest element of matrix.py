# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 06:54:26 2024

@author: Admin
"""
#Biggest element of matrix.
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
    
biggest=0
i=0
while i<rows:
    j=0
    while j<cols:
        if m[i][j]>biggest:
            biggest=m[i][j]
        else:
            pass
        j=j+1
    i=i+1
print(biggest)