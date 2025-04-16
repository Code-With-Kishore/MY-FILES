# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:18:57 2024

@author: Admin
"""

x=0
y=0
b=0
c=0

a=int(input('Enter a value:'))
while a!=1000:
    if a>0:
        b=a+b
        x=x+1
    elif a<0:
        c=a+c
        y=y+1
    else:
        print('zero')
    a=int(input('Enter a value:'))
    d=b/x
    e=c/y
    print(d)
    print(e)
    