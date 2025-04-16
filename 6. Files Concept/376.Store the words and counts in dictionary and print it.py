# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 05:51:18 2024

@author: Admin
"""
d={}
f=open('project.txt','r')
y=1
for i in f:
    words=i.split()
    counts=len(words)
    values=[words, counts]
    d[y]=values
    print(d)
    y=y+1
f.close()