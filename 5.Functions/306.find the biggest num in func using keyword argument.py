# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 05:46:55 2024

@author: Admin
"""

def biggest(a=10,b=20,c=30):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x
#main

n=biggest()
x=biggest(b=10)
y=biggest(b=10,a=20)
z=biggest(a=30,b=20,c=10)

print(n)
print(x)
print(y)
print(z)