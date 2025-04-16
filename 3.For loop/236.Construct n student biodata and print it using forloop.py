# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 05:07:33 2024

@author: Admin
"""
s=[]
n=int(input('Enter the value:'))
for i in range(n):
    a=input('Enter the name:')
    b=int(input('Enter the age:'))
    c=input('Enter the qualification:')
    d=int(input('Enter the mobile no.'))
    e=input('Enter the location:')
    x=[a,b,c,d,e]
    for i in x:
        print(i)