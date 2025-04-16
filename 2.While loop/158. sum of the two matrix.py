# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 07:17:48 2024

@author: Admin
"""

m1=[]
m2=[]
sum=[]
rows=3
cols=3
i=0
while i<rows:
    row=[]
    j=0
    while j<cols:
        a=int(input('Enter a matrix 1 value:'))
        row.append(a)
        j=j+1
    m1.append(row)  
    i=i+1
    
m2=[]
rows=3
cols=3
i=0
while i<rows:
    row=[]
    j=0
    while j<cols:
        a=int(input('Enter a matrix 2 value:'))
        row.append(a)
        j=j+1
    m2.append(row)  
    i=i+1
    
sum=[]
i=0
while i<rows:
    row=[]
    j=0
    while j<cols:
        e=m1[i][j]+m2[i][j]
        row.append(e)
        j=j+1 
    sum.append(row)
    i=i+1
    
i=0
while i<rows:
    j=0
    while j<cols:
        print(sum[i][j])
        j=j+1
    i=i+1