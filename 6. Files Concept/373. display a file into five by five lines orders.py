# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 04:12:08 2024

@author: Admin
"""

f=open('project.txt','r')
y=1
for i in f:
    print(y, i)
    y=y+1
    
    if y%5==0:
        input('Enter to continue')
f.close()


    