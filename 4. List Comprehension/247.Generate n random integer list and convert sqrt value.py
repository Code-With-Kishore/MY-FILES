# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 06:31:50 2024

@author: Admin
"""
import random
import math
n=int(input('Generate n random int value:'))
x=[random.randint(1,100)for i in range(n)]
y=[math.sqrt(j)for j in x]
print(x)
print(y)