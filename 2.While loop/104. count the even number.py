# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:07:56 2024

@author: Admin
"""
x=0
a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
while a<=b:
    r=a%2
    if r==0:
        x=x+1  
    else:
        print('odd')
    a=a+1
    print(x)