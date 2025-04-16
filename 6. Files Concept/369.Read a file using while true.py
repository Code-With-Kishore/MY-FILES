# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:29:10 2024

@author: Admin
"""

f=open('project.txt', 'r')
x=f.read()
while True:
    print(x, end='')
    x=f.read()
f.close()