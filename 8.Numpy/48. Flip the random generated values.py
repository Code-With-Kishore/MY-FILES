# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:23:33 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
a=np.random.randint(0, 100, n)
x=np.flip(a)
print('Random Generated values:',a)
print('Flip values:',x)