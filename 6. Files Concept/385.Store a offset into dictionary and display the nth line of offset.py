# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 04:24:25 2024

@author: Admin
"""

x=open('task.txt','r')
d={}
offset=0
y=1
for i in x:
    ln=len(i)
    values=[offset, ln, i]
    offset=offset+ln+1
    d[y]=values
    y=y+1
print(d)

n=int(input('Enter nth value:'))
x.seek(d[n][0])
z=x.readline()
print(z)
