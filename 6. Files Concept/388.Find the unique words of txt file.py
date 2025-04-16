# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:48:59 2024

@author: Admin
"""

f=open('task2.txt','r') #Machine learning is the future of technology and innovation.
f1=open('task.txt','r') #Datascience and machinelearning are the fascinating fields.


x=f.read()
y=x.split()
z=set(y)

a=f1.read()
b=a.split()
c=set(b)

d=z-c

print(d)

f.close()
f1.close()