# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:16:26 2024

@author: Admin
"""

a=int(input('Enter a value:'))
while a!=1000:
    if a>0:
        print('positive')
    elif a<0:
        print('negative')
    else:
        print('zero')
    a=int(input('Enter a value:'))
   