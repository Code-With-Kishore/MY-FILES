# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:18:44 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter no.of.data: '))
marks=np.random.randint(0, 100, n, dtype='uint8')
year=np.random.randint(0, 65535, n, dtype='uint16')
kilometer=np.random.randint(0, 65535, n, dtype='uint16')
space_travel=np.random.randint(0, 384400, n, dtype='uint32')

print('Marks',marks)
print('Years',year)
print('Kilometer',kilometer)
print('Space travel distance',space_travel)