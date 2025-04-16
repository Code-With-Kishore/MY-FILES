# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 05:30:14 2024

@author: Admin
"""

x=open('project.txt','r')
y=open('task2.txt','w')
for i in x:
    for j in i:
        y.write(j)
x.close()
y.close()
