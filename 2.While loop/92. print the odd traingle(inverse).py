# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:40:09 2024

@author: Admin
"""

x=0
y=7
a=1
while a<=4:
    b=1
    while b<=x:
        print(' ', end='')
        b=b+1
    c=1
    while c<=y:
        print('*', end='')
        c=c+1
    a=a+1
    y=y-2
    x=x+1
    print()