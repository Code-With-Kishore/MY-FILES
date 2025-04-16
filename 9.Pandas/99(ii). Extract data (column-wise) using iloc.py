# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 10:26:51 2025

@author: Admin
"""
import pandas as pd
import numpy as np
sub = ['tamil', 'english', 'maths', 'science', 'social']
roll = [225213101 + i for i in range(20)]
m = np.random.randint(0, 100, (20, 5), dtype=np.uint8)
x = pd.DataFrame(m, index=roll, columns=sub)
print(x)
f2 = x.iloc[:, :2]
print("\nFirst 2 columns:\n", f2)
m1 = x.iloc[:, 2:3]
print("\nMiddle one column:\n", m1)
l2 = x.iloc[:, -2:]
print("\nLast 2 columns:\n", l2)