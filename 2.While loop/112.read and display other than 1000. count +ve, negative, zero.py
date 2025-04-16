# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:32:39 2024

@author: Admin
"""
x=0
y=0
z=0
a=int(input('Enter a value:'))
while a!=1000:
    if a>0:
        x=x+1
    elif a<0:
        y=y+1
    else:
        z=z+1
    a=int(input('Enter a value:'))
    print(x)
    print(y)
    print(z)
    
        
   