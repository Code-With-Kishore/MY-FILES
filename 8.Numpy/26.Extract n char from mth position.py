# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:12:35 2025

@author: Admin
"""

import numpy as np
f1=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f1, dtype='uint8')
n=int(input('Enter n value:'))
m=int(input('Enter mth position value: '))
f2=x[m:m+n]
print(f2)