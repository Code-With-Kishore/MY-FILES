# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:57:02 2025

@author: Admin
"""

import numpy as np
f=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f, dtype='uint8')

for i in x:
    print(chr(i), end='')