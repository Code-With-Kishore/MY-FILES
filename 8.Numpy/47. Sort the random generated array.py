# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:03:28 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
a=np.random.randint(0, 100, n)
x=np.sort(a)
print('Random Generated values:',a)
print('Sorted values:',x)