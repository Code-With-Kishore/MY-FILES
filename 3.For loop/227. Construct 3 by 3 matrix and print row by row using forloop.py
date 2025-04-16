# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 07:20:39 2024

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


for k in m:
    print(k)
    