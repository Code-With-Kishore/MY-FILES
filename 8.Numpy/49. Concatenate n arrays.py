# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:40:07 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))

a=np.random.randint(0, 50, n)
b=np.random.randint(50, 100, n)
x=np.concatenate((a,b))

print('Random values 1:',a)
print('Random values 2:',b)
print('Concatenate values:',x)