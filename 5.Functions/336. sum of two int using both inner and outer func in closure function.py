# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 06:57:21 2024

@author: Admin
"""

def cal(a):
    def sum(b):
        c=a+b
        return c
    return sum
    
#main
a=int(input('Enter the a value:'))
b=int(input('Enter the b value:'))
x=cal(a)
print(x(b))
