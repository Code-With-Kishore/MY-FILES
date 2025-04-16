# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:40:39 2024

@author: Admin
"""

def calculate():
    def biggest(a,b,c):
        d=(a if a>c else c) if a>b else(b if b>c else c)
        return d
    a=int(input('Enter a value:'))
    b=int(input('Enter b value:'))
    c=int(input('Enter c value:'))
    x=biggest(a,b,c)
    print(x)
    
#main
calculate()