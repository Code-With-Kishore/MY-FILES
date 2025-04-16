# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 05:41:33 2024

@author: Admin
"""

def calculate(a,b):
    def sum():
        c=a+b
        return c
    result=sum()
    print(result)
    
#main
a=int(input('Enter the a value:'))
b=int(input('Enter the b value:'))
calculate(a,b)