# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:35:20 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n data value: '))
a=np.random.randint(-32768, 32767, n, dtype='int16')
f=open('C:/Users/Admin/Documents/Python/Data Science/mydatads', 'wb')
a.tofile(f)
f.close()