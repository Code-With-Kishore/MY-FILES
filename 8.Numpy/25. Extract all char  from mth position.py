# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:59:26 2025

@author: Admin
"""

import numpy as np
f1=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f1, dtype='uint8')
m=int(input('Enter mth position value: '))
f2=x[m:]
print(f2)