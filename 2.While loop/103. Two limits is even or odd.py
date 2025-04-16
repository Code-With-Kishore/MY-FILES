# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:03:40 2024

@author: Admin
"""

a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
while a<=b:
    c=a%2
    if c==0:
        print('Even')
    else:
        print('odd')
    a=a+1