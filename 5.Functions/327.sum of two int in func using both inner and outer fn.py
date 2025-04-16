# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:05:57 2024

@author: Admin
"""

def calculate(a):
    
    def sum(b):
        c=a+b
        return c
    b=int(input('Enter b value:'))
    result=sum(b)
    print(result)
    
#main
a=int(input('Enter a value:'))
calculate(a)