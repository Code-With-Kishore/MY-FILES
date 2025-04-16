# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:28:34 2024

@author: Admin
"""

m=[]
r=3
c=3
for i in range(1,r+1):
    row=[]
    for j in range(1,c+1):
        d=int(input('Enter matrix value:'))
        row.append(d)
    m.append(row)
    
b=0
for k in m:
    for l in k:
        b=l if l>b else b
print(b)