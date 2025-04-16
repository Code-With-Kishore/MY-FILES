# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 05:44:26 2024

@author: Admin
"""


import random
def square(a):
    b=a*a
    return b

#main
n=int(input('Enter n values:'))
x=[random.randint(1,100)for i in range(n)]
y=map(square,x)
z=list(y)
print('list',x)
print('square value of the lists are:',z)