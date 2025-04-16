# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 06:41:32 2024

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
    x=d(i) 
    print(a,'*',i,'=',x)