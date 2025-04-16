# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 04:40:57 2024

@author: Admin
"""

f=open('project.txt','r')
d={}
y=1
for i in f:
    length=len(i)
    words=i.split()
    ln=len(words)
    values=[length, i, words, ln]
    d[y]=values
    y=y+1
    
b=0
for i in d:
    if d[i][3]>b:
        b=d[i][3]
        c=i
f.close()
print(c, d[c][1])
