# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 19:48:56 2025

@author: Admin
"""

import numpy as np
r=int(input('Enter row value:'))
c=int(input('Enter cols value:'))
m=np.random.randint(-100, 100, (r,c))
file=open('C:/Users/Admin/Documents/Python/Data Science/matrix','wb')
m.tofile(file)
file.close()
print('Your Data Stored Successfully...')