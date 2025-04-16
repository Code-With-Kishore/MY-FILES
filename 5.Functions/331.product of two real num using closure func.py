# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 05:48:13 2024

@author: Admin
"""

def cal(a,b):
    def pro():
        c=a*b
        return c
    return pro
#main
a=int(input('Enter a:'))
b=int(input('Enter b:'))
x=cal(a,b)
print(x())