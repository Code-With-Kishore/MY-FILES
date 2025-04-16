# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:07:34 2024

@author: Admin
"""
x=4
y=1

d=1
while d<=5:
    print(' ', end='')     
    d=d+1
print('*', end='')
print()

a=1
while a<=4:
    b=1
    while b<=x:
        print(' ', end='')
        b=b+1
    print('*', end='')    
    c=1
    while c<=y:
        print(' ', end='')
        c=c+1
    print('*', end='')   
    a=a+1
    x=x-1
    y=y+2
    print()
    
i=1
while i<=6:
    print('* ', end='')
    i=i+1