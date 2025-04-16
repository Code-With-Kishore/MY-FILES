# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:07:50 2025

@author: Admin
"""

import pandas as pd
import numpy as np

sub = ['tamil', 'english', 'maths', 'science', 'social']
roll = [225213101 + i for i in range(20)]

m = np.random.randint(0, 100, (20, 5), dtype=np.uint8)

x = pd.DataFrame(m, index=roll, columns=sub)
print("Full DataFrame:\n", x)

a = x.loc[225213101:225213105]  
print("\nFirst 5 rows:\n", a)

m10 = x.loc[225213106:225213115] 
print("\nMiddle 10 rows:\n", m10)

l5 = x.loc[225213116:225213120]  
print("\nLast 5 rows:\n", l5)
