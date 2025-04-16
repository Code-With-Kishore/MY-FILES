# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:27:28 2024

@author: Admin
"""

x=y=0
a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
while a<=b:
    r=a%4
    if r==0:
        x=x+1
    else:
        y=y+1
    a=a+1
    print(x)
    print(y)