# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:39:24 2025

@author: Admin
"""

import numpy as np
f1=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f1, dtype='uint8')
n=int(input('Enter n value:'))
ln=len(x)-n
f2=x[ln:]
print(f2)