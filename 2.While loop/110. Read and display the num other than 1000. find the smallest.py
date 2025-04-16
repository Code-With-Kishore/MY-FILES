# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:04:14 2024

@author: Admin
"""

a=9999
b=int(input('Enter b value:'))
while a!=1000:
    if a<b:
        b=a
    else:
        print('not')
        a=int(input('Enter a value:'))
    print(b)
    