# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 05:13:53 2024

@author: Admin
"""

def calculate(a):
    def mul(b):
        c=a*b
        return c
    return mul
#main
a=int(input('Enter value of a:'))
n=int(input('Enter n value:'))
d=calculate(a)
for i in range(n):
    print(d(i))
 
    