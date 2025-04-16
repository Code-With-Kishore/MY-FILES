# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 06:12:51 2024

@author: Admin
"""

def product(a,b):
    c=a*b
    return c
def mul(a,b,x):
    d=x(a,b)
    print(d)
#main
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
mul(a,b,product)