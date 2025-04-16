# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:29:43 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
a=np.random.randint(0, 500, n)
unique, count=np.unique(a, return_counts=True)
print('Random Generated Array: ', a)
print('Unique values: ', unique)
print('Count Unique values: ', count)