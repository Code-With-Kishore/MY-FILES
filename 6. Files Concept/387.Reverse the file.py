# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:35:40 2024

@author: Admin
"""

x=open('task.txt','r')
d={}
offset=0
line=1
for i in x:
    ln=len(i)
    values=[offset, ln, i]
    offset=offset+ln+1
    d[line]=values
    line=line+1
for j in range(line-1,0,-1):
    x.seek(d[j][0])
    z=x.readline()
    print(z,end='')
x.close()
