# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:02:39 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
a=np.random.randint(0, 1000, n)
x,y,z=np.split(a, 3)
print('Random Generated Array: ', a)
print('Split array into equal part 1: ', x)
print('Split array into equal part 2: ', y)
print('Split array into equal part 3: ', z)
