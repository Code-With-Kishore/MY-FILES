# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:38:40 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
x=np.random.randint(-128, 127, n)
p=x>=0
n=x<=0
ap=x[p]
an=x[n]

print('Random Generated values: ', x)
print('Positive: ', p)
print('Negative: ', n)
print('Actual Positive no: ', ap)
print('Actual Negative no: ', an)