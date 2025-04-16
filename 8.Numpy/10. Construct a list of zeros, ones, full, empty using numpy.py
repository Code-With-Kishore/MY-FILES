# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 04:50:02 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value:'))

a=np.zeros(n)
b=np.ones(n)
c=np.full(n, 3)
d=np.empty(n)

print('Zeros:',a)
print('Ones:',b)
print('Full:',c)
print('Empty',d)