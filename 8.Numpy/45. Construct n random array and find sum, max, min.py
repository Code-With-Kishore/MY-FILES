# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:02:21 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
x=np.random.randint(0, 1000, n)
i=x.max()
j=x.min()
k=x.sum()
print('Random Generate Number:', x)
print('Maximum of array: ', i)
print('Minimum of array: ', j)
print('Sum of array:', k)