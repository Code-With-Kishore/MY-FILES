# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 10:39:42 2025

@author: Admin
"""


import pandas as pd
import numpy as np
roll = [225213101 + i for i in range(20)]
mis_d=[225213113,223213102,225213112]
sub = ['tamil', 'english', 'maths', 'science', 'social']
m = np.random.randint(50, 100, (20, 5), dtype=np.uint32)
x = pd.DataFrame(m, index=roll, columns=sub)
for i in mis_d:
    x.loc[i]  =pd.NA
print('\nData\n', x)

x=x.dropna()
print('\nData\n', x)
