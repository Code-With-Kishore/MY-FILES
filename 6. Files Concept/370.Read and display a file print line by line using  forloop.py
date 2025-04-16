# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:52:14 2024

@author: Admin
"""

f=open('project.txt', 'r')
x=f.read()
for i in x:
    print(i, end='')
f.close()
    