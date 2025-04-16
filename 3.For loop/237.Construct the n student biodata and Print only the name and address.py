# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:39:59 2024

@author: Admin
"""

s=[]
n=int(input('Enter the n student value:'))
for i in range(n):
    a=input('Enter the name:')
    b=int(input('Enter the age:'))
    c=input('Enter the qualification:')
    d=int(input('Enter the mobile no.'))
    e=input('Enter the location:')
    x=[a,b,c,d,e]
    s.append(x)
    for j in s:
        print(j[0])
        print(j[4])
        