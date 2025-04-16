# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 04:53:54 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value:'))
a=np.random.randint(0, 100, n)
b=a.shape
c=a.size
d=a.dtype
e=a.itemsize
f=a.nbytes
g=a.ndim
print(a)
print('shape of array:',b)
print('size of array:',c)
print('data type of array:',d)
print('item size:',e)
print('no.of.bytes:',f)
print('no.of.dimension:',g)
