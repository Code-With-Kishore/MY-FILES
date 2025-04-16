# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 05:49:55 2024

@author: Admin
"""

def calculate(a,b,c):
    def biggest():
        d=(a if a>c else c)if a>b else(b if b>c else c)
        return d
    result=biggest()
    print(result)
    
#main
a=int(input('Enter the a value:'))
b=int(input('Enter the b value:'))
c=int(input('Enter the c value:'))
calculate(a,b,c)