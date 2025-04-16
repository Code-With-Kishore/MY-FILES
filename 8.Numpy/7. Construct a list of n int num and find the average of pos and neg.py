# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 04:32:29 2025

@author: Admin
"""

import random
import numpy as np
n=int(input('Enter n value:'))
a=[random.randint(-100,100) for i in range(n)]
b=np.array(a)
print(b)

c=0
d=0

P_count=0
N_count=0

for i in b:
    if i>0:
        c+=i
        P_count+=1
    elif i<0:
        d+=i
        N_count+=1
    else:
        pass

e=c/P_count
f=d/N_count

print('Average of positive:', e)
print('Average of negative:', f)
