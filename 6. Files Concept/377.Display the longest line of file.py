# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:10:11 2024

@author: Admin
"""

f=open('project.txt','r')
d={}
y=1
for i in f:
    length=len(i)
    words=i.split()
    values=[length, i, words]
    d[y]=values
    y=y+1
    
b=0
for i in d:
    if d[i][0]>b:
        b=d[i][0]
        c=i
    f.close()
print(c, d[c][1])

