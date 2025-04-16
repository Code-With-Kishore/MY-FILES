# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 05:24:37 2024

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

common_words=file1.intersection(file2)
ln=len(common_words)

find_total=file1.union(file2)
total=len(find_total)
percentage=(ln / total *100)

print('Common Words b/w two files:',common_words)
print('Percentage of Common Words:',percentage)