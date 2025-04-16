# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 06:37:23 2024

@author: Admin
"""
import random
n=int(input('Enter n random int value :'))
x=[random.randint(1,101)for i in range(n)]
y=[random.randint(1,101)for j in range(n)]
z=[x[k]+y[k] for k in range(n)]
print('generated list of x is:',x)
print('generated list of y is:',y)
print('Sum of x and y value is',z)