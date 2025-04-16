# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 05:58:11 2025

@author: Admin
"""

import random
import numpy as np
n=int(input('Enter n value:'))
a=[random.randint(-1000,1000) for i in range(n)]
b=np.array(a)
print(b)

s_count=0
t_count=0
three_count=0

for i in b:
    if i>0 and i<9:
        s_count+=1
    elif i>10 and i<99:
        t_count+=1
    elif i>100 and i<999:
        three_count+=1
    else:
        pass
        

print('single count:', s_count)
print('two count:', t_count)
print('three count:', three_count)
