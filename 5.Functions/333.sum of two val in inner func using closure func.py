# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 06:03:40 2024

@author: Admin
"""

def cal():
    def sum(a,b):
        c=a+b
        return c
    return sum
#main
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
x=cal()
print(x(a,b))