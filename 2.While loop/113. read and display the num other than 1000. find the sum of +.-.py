# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:08:53 2024

@author: Admin
"""

x=0
y=0

a=int(input('Enter a value:'))
while a!=1000:
    if a>0:
        x=a+x
    elif a<0:
        y=a+y
    else:
        print('zero')
    a=int(input('Enter a value:'))
    print(x)
    print(y)
    