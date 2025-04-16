# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 05:49:00 2024

@author: Admin
"""

def sum(a,b):
    c=a+b
    return c
 
def my_func(a,b,k):
    s=k(a,b)
    print(s)
    
#main
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
my_func(a,b,sum)