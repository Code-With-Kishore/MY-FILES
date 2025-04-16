# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:47:07 2025

@author: Admin
"""

import numpy as np
mean=int(input('Enter mean value:'))
standard_dev=int(input('Enter sd value:'))
n=int(input('Enter n value:'))
x= np.random.normal(mean, standard_dev, n)
print(x)