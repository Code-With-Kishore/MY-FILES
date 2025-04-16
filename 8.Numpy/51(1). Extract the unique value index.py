# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:17:10 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
a=np.random.randint(0, 500, n)
unique, index=np.unique(a, return_index=True)
print('Random Generated Array: ', a)
print('Unique values: ', unique)
print('Index of unique values: ', index)