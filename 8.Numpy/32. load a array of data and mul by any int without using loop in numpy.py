# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:01:07 2025

@author: Admin
"""

import numpy as np
f = open("D:\data1.txt","r")
a = np.fromfile(f,dtype=np.uint8)
f = open("D:\data1.txt","r")
a = np.fromfile(f,dtype=np.uint8)
mul = a**2

print('Entire original data: ',a)
print('Entire data mul by 2: ',mul)

