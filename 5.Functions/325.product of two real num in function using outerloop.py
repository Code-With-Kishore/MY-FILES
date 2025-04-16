# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 05:46:22 2024

@author: Admin
"""

def calculate(a,b):
    def product():
        c=a*b
        return c
    result=product()
    print(result)
    
#main
a=int(input('Enter the a value:'))
b=int(input('Enter the b value:'))
calculate(a,b)