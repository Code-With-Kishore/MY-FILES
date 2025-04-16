# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:16:50 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
a=np.random.randint(0, 1000, n)
x=np.unique(a)
print('Random Generated Array: ', a)
print('Extract the unique values: ', x)