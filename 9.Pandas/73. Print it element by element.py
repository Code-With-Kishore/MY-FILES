# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 19:07:18 2025

@author: Admin
"""

import numpy as np
import pandas as pd
n=int(input('Enter n value: '))
x=pd.Series(data=np.random.randint(0, 100, n))
print(x)

ln=len(x)
for i in range(ln):
    print(x[i])
    