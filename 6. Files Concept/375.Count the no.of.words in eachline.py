# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 04:53:17 2024

@author: Admin
"""

f=open('project.txt', 'r')
y=1
for i in f:
    words=i.split()
    ln=len(words)
    print('Lines:',y, 'Count:',ln)
    y=y+1
f.close()