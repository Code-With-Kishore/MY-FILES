# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 06:15:42 2024

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


for j in range(1,line,2):
    x.seek(d[j][0])
    y=x.readline()
    print(y)
x.close()