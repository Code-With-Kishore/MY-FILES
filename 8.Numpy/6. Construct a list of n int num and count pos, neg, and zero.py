# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 05:39:51 2025

@author: Admin
"""

import random
import numpy as np
n=int(input('Enter n value:'))
a=[random.randint(-100,100) for i in range(n)]
b=np.array(a)
print(b)

P_count=0
N_count=0

for i in b:
    if i>0:
        P_count+=1
    elif i<0:
        N_count+=1
    else:
        pass

print('positive count:', P_count)
print('negative count:', N_count)

        