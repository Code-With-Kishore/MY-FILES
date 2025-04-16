# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 05:09:03 2024

@author: Admin
"""

x=open('project.txt','r')
y=open('task2.txt','w')
for i in x:
    for j in i:
        u=ord(j)
        if u>=65 and u<=90:
           a=u+32
           b=chr(a)
           y.write(b)
        elif u>=97 and u<=122:
             c=u-32
             d=chr(c)
             y.write(d)
        else: 
            y.write(j)
x.close()
y.close()
