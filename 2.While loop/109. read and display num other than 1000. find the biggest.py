# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:48:57 2024

@author: Admin
"""

b=0
a=int(input('Enter a value:'))
while a!=1000:
    if a>b:
        b=a
    else:
        print('not')
        a=int(input('Enter a value:'))
    print(b)
