# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:36:24 2024

@author: Admin
"""

def biggest_of_three_num(a,b,c):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x
#main
a=int(input('Enter A value:'))
b=int(input('Enter B value:'))
c=int(input('Enter C value:'))
x=biggest_of_three_num(a,b,c)
print('Biggest value is:',x)