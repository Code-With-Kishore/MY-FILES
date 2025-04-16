# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:49:31 2025

@author: Admin
"""

import numpy as np
f1=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f1, dtype='uint8')
n=int(input('Enter n value: '))
f2=x[0:n]
print(f2)
