# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 04:33:15 2024

@author: Admin
"""

f=open('project.txt', 'r')
y=1
for i in f:
    ln=len(i)
    print('Lines:',y, 'Length:',ln)
    y=y+1
f.close()