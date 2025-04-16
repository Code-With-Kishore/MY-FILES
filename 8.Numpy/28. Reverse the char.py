# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:55:37 2025

@author: Admin
"""

import numpy as np
f1=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f1, dtype='uint8')
f2=x[::-1]
print(f2)