# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 06:09:12 2024

@author: Admin
"""

f=open('project.txt','r')
offset=0
x=1
for i in f:
    ln=len(i)
    print('Offset:',offset,'Length:',ln, i)
    offset=offset+ln
    x=x+1
f.close()