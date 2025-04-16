# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 06:56:39 2024

@author: Admin
"""

x=1
y=5
a=1
while a<=3:
    b=1
    while b<=x:
        print(' ', end='')
        b=b+1
        
    c=1
    while c<=y:
        print(c, end='')
        c=c+1
    a=a+1
    x=x+1
    y=y-2
    print()