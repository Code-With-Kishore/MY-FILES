# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:27:38 2025

@author: Admin
"""

import numpy as np
f1=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f1, dtype='uint8')
n=int(input('Enter n value: '))
f2=x[-1:-n:-1]
print(x)
print('Copy the last n character: ',f2)