# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:32:51 2024

@author: Admin
"""

def calculate():
    def sum(a,b):
        c=a+b
        return c
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    x=sum(a,b)
    print(x)
    
#main
calculate()