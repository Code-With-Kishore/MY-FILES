# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 05:36:17 2024

@author: Admin
"""

x=open('project.txt','r')
y=open('task2.txt','r')
z=open('task.txt','w')
for i in x:
    z.write(i)
for j in y:
    z.write(j)
x.close()
y.close()
z.close()

