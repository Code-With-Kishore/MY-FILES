# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 05:57:05 2024

@author: Admin
"""

x=3
y=1
a=1
while a<=4:
    b=1
    while b<=x:
        print(' ',end='')
        b=b+1
    c=1
    while c<=y:
        print(chr(96+c), end='')
        c=c+1
    a=a+1
    x=x-1
    y=y+2
    print()
    
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
        print(chr(96+c), end='')
        c=c+1
    a=a+1
    x=x+1
    y=y-2
    print()
    