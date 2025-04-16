# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 06:36:38 2024

@author: Admin
"""

def cal():
    def biggest(a,b,c):
        d=( a if a>c else c )if a>b else(b if b>c else c) 
        return d
    return biggest
#main
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
x=cal()
print(x(a,b,c))