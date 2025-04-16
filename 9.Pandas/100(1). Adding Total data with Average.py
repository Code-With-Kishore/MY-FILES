# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:10:35 2025

@author: Admin
"""

import pandas as pd
import numpy as np

sub = ['tamil', 'english', 'maths', 'science', 'social']
roll = [225213101 + i for i in range(20)]

m = np.random.randint(0, 100, (20, 5), dtype=np.uint8)

x = pd.DataFrame(m, index=roll, columns=sub)
print(x)

t = x['tamil']+ x['english']+ x['maths']+x['science']+ x['social']

x['Total'] = t

print("\nData with Total Marks:\n", x)

avg = t/len(x)

x['average'] = avg

print('\nTotal data with Average\n', x)