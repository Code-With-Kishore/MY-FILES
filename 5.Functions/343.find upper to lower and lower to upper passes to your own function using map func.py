# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:05:10 2024

@author: Admin
"""

def flip(u):
    u=ord(u)
    if u>=65 and u<=90:
        a=u+32
        x=chr(a)
        return x
    elif u>=97 and u<=122:
        b=u-32
        y=chr(b)
        return y
    else:
        z=chr(u)
        return z
    
#main
a=input('Enter the string:')
b=map(flip,a)
for j in b:
    print(j, end='')
        
    