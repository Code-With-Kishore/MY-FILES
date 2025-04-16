# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 08:40:12 2024

@author: Admin
"""

y=5
x=0
a=1
while a<=5:
    b=1
    while b<=x:
        print('-', end='')
        b=b+1
    c=1
    while c<=y:
        print('*', end='')
        c=c+1
    a=a+1
    x=x+1
    y=y-1
    print()