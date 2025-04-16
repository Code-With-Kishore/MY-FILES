# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 05:15:46 2024

@author: Admin
"""

x=open('project.txt','r')
y=open('python.txt','w')
for i in x:
    y.write(i)
x.close()
y.close()