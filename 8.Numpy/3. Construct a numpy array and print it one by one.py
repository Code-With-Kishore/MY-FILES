# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 04:59:59 2025

@author: Admin
"""

import random
import numpy as np
n=int(input('Enter n value:'))
a=[random.randint(1,1000)for i in range(n)]
b=np.array(a)

for i in b:
    print(i)
