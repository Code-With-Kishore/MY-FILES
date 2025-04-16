# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:01:21 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
a=np.random.randint(0, 1000, n)
x=np.split(a, 5)
print('Random Generated Array: ', a)
print('Split array into n equal parts: ', x)