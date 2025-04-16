# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 05:17:34 2024

@author: Admin
"""


f1=open('task.txt','r') 
a=f1.read()
b=a.split()
c=set(b)

f2=open('task2.txt','r')
d=f2.read()
e=d.split()
f=set(e)

f3=open('project.txt','r')
g=f3.read()
h=g.split()
i=set(h)

j=c-i
k=f-i

file1=set(j)
file2=set(k)

common=file1.intersection(file2)

print(common)