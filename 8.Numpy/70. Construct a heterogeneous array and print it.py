# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 18:52:09 2025

@author: Admin
"""

import numpy as np

d = [('name', np.str_, 10),  
     ('age', np.int8), 
     ('percent', np.float32)]

x = [('kishore', 23, 75.5)]  

y = np.array(x, d)

print(y)
