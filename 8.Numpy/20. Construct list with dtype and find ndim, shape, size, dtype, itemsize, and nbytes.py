# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:15:18 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value:'))
l=np.random.randint(-128, 127, n, dtype='int8')
print('ndimension', l.ndim)
print('shape' ,l.shape)
print('size', l.size)
print('dtype', l.dtype)
print('itemsize' ,l.itemsize)
print('nbytes' ,l.nbytes)
