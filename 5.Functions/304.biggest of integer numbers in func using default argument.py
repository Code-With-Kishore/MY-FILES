# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:50:12 2024

@author: Admin
"""

def biggest(a=100,b=500,c=300):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x
#main

n=biggest()
x=biggest(500)
y=biggest(800,600)
z=biggest(900,100,200)

print(n)
print(x)
print(y)
print(z)