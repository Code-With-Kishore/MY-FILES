# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 17:38:05 2025

@author: Admin
"""

import pandas as pd
import numpy as np

roll = [225213101 + i for i in range(20)]
mis_d = [225213113, 223213102, 225213112]
sub = ['Tamil', 'English', 'Maths', 'Science', 'Social']
m = np.random.randint(50, 100, (20, 5), dtype=np.uint32)
x = pd.DataFrame(m, index=roll, columns=sub)
print(x)

s = x.apply(np.sum, axis=1)
print('\nSum of individual student marks\n', s)

max_val=np.argmax(s)
max_ind=x.index[max_val]
print('\nMax-index value\n',max_ind)

a=x.loc[max_ind]
print('\nTopper Student Marks\n',a)


