# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:27:32 2024

@author: Admin
"""


def cal(a,b):
    def sum():
        c=a+b
        return c
    return sum
#main
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
x=cal(a,b)
print(x())