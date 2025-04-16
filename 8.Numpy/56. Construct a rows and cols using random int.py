# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 18:47:13 2025

@author: Admin
"""

import numpy as np
r=int(input('Enter rows value: '))
c=int(input('Enter cols value: '))
m=np.random.randint(-100, 100, (r,c))
print(m)