# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 05:47:20 2024

@author: Admin
"""

def biggest_and_smallest(a=10,b=20,c=30):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    y=(a if a<c else c)if a<b else(b if b<c else c)
    return x,y

#main
a=biggest_and_smallest()
b=biggest_and_smallest(c=10)
c=biggest_and_smallest(b=20,a=10)
d=biggest_and_smallest(c=10,b=20,a=30)

print(a)
print(b)
print(c)
print(d)