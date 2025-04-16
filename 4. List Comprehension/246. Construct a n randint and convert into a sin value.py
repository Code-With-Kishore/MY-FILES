# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 04:52:03 2024

@author: Admin
"""
import math
import random
n=int(input('Enter the value:'))
x=[i for i in range(n)]
y=[math.sin(random.randint(1,101))for j in x]
print(x)
print(y)