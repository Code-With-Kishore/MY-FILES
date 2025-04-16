# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:36:47 2024

@author: Admin
"""

m1=[]
m2=[]
sum=[]
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
    
sum=[]
for i in range(3):
    row=[]
    for j in range(3):
        z=m1[i][j]+m2[i][j]
        row.append(z)
    sum.append(row)
    
for k in sum:
    print(k)