# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 07:12:32 2024

@author: Admin
"""
#Biggest element of each row.
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
    biggest=0
    j=0
    while j<cols:
        if m[i][j]>biggest:
            biggest=m[i][j]
        j=j+1
    print(biggest)
    i=i+1
    
    