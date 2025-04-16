# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 06:34:53 2024

@author: Admin
"""

def cal():
    def prod(a,b):
        c=a*b
        return c
    return prod
#main
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
x=cal()
print(x(a,b))