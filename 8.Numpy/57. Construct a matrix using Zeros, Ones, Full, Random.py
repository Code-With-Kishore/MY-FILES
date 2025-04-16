# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 19:21:49 2025

@author: Admin
"""

import numpy as np
r=int(input('Enter row value: '))
c=int(input('Enter col value: '))
z=np.zeros((r,c))
o=np.ones((r,c))
f=np.full((r,c), 31)
r=np.random.random((r,c))

print('Zeros:',z)
print('Ones:',o)
print('Full:',f)
print('Random:',r)