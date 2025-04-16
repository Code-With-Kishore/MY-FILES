# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 05:31:57 2024

@author: Admin
"""

m1=[]
m2=[]
subraction=[]
r=3
c=3
for i in range(0,r):
    row1=[]
    for j in range(0,c):
        d1=int(input('Enter matrix 1 value:'))
        row1.append(d1)
    m1.append(row1)
    

r=3
c=3
for i in range(0,r):
    row2=[]
    for j in range(0,c):
        d2=int(input('Enter matrix 2 value:'))
        row2.append(d2)
    m2.append(row2)


subraction=[]
for i in range(0,r):
    row=[]
    for i in range(0,c):
        z=m1[i][j]-m2[i][j]
        row.append(z)
    subraction.append(row)
    
for k in subraction:
    print(k)

