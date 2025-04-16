# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:25:09 2024

@author: Admin
"""

def calculate(x):
    def mul(y):
        z=x*y
        return z
    return mul
#main
x=int(input('Enter value of a:'))
y=int(input('Enter value of b:'))
result=calculate(x)
print(result(y))  