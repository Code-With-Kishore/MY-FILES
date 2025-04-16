# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 05:50:06 2024

@author: Admin
"""

def cal(a,b,c):
    def biggest():
        d=( a if a>c else c )if a>b else(b if b>c else c) 
        return d
    return biggest
#main
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
x=cal(a,b,c)
print(x())