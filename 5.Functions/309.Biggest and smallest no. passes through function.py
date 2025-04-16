# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 05:03:34 2024

@author: Admin
"""

def biggest_and_smallest(*arg):
    b=0
    s=9999
    for i in arg:
        b=i if i>b else b
        s=i if i<s else s
    return b,s
#main
a=biggest_and_smallest(1,2,3,4,5,6,7,8,9,10)
b=biggest_and_smallest(100,200,300,400,500)
c=biggest_and_smallest(1000,2000,3000,4000,5000)
print(a)
print(b)
print(c)