# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:36:20 2024

@author: Admin
"""

def calculate():
    def product(a,b):
        c=a*b
        return c
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    x=product(a,b)
    print(x)
    
#main
calculate()
