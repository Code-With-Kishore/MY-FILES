# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:06:49 2025

@author: Admin
"""

import numpy as np
f=open("D:\data1.txt","r")
a=np.fromfile(f,dtype=np.uint8)
s=len(a)
d=s//4

f1=a[:d]
f2=a[d:d*2]
f3=a[d*2:d*3]
f4=a[d*3:]

print('length of data: ',s)
print('part1: ',f1)
print('part2: ',f2)
print('part3: ',f3)
print('part4: ',f4)
