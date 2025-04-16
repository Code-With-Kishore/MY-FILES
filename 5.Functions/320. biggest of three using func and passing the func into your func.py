# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 06:29:45 2024

@author: Admin
"""

def biggest(a,b,c):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x

def largest_val(a,b,c,x):
    d=x(a,b,c)
    print(d)
    
#main
a=int(input('Enter the a value:'))
b=int(input('Enter the b value:'))
c=int(input('Enter the c value:'))
largest_val(a,b,c,biggest)