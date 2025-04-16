# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:07:16 2024

@author: Admin
"""

f=open('project.txt', 'r')
y=1
for i in f:
    print(y,i)
    y=y+1
f.close()