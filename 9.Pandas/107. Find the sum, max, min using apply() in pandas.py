# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 12:13:58 2025

@author: Admin
"""

import pandas as pd
import numpy as np
roll = [225213101 + i for i in range(20)]
mis_d=[225213113,223213102,225213112]
sub = ['tamil', 'english', 'maths', 'science', 'social']
m = np.random.randint(50, 100, (20, 5), dtype=np.uint32)
x = pd.DataFrame(m, index=roll, columns=sub)
print(x)

#row-wise sum, max, min
s=x.apply(np.sum, axis=1)
big=x.apply(np.max, axis=1)
small=x.apply(np.min, axis=1)

#column-wise sum, max, min
c_big=x.apply(np.max, axis=0)
c_small=x.apply(np.min, axis=0)


print('\nSum\n',s)
print('\nMaximum Mark of each student\n',big)
print('\nMinimum Mark of each student\n',small)

print('\nMaximum Mark (column-wise)\n', c_big)
print('\nMinimum Mark (column-wise)\n',c_small)