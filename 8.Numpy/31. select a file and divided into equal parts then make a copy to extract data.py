# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:38:21 2025

@author: Admin
"""

import numpy as np
f=open("D:\data1.txt","r")
a=np.fromfile(f,dtype=np.uint8)
s=len(a)
d=s//4

part1=a[:d].copy()
part2=a[d:d*2].copy()
part3=a[d*2:d*3].copy()
part4=a[d*3:].copy()

print('length of data: ',s)
print('part1: ',part1)
print('part2: ',part2)
print('part3: ',part3)
print('part4: ',part4)
