# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:35:50 2024

@author: Admin
"""

x=open('project.txt','r')
d={}
offset=0
y=1
for i in x:
    ln=len(i)
    values=[offset, ln, i]
    offset=offset+ln
    d[y]=values
    y=y+1
x.close()
print(d)
