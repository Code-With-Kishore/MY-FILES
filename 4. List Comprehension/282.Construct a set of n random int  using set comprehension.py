# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 05:44:26 2024

@author: Admin
"""

#Construct a set of n random integer numbers using set comprehension.
import random
n=int(input('Enter n values:'))
x={random.randint(0,100) for i in range(n)}
print(x)
