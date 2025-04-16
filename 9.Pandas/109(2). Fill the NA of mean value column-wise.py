# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 18:33:43 2025

@author: Admin
"""

import pandas as pd
import numpy as np

roll = [225213101 + i for i in range(20)]
absent = [225213102, 225213106, 225213108, 225213109]
sub = ['tamil', 'english', 'maths', 'science', 'social']
m = np.random.randint(50, 100, (20, 5), dtype=np.uint16)
x = pd.DataFrame(m, index=roll, columns=sub)

for i in absent:
    x.loc[i] = pd.NA  

x['tamil'] = x['tamil'].fillna(value=x['tamil'].mean())
x['english'] = x['english'].fillna(value=x['english'].mean())
x['maths'] = x['maths'].fillna(value=x['maths'].mean())
x['science'] = x['science'].fillna(value=x['science'].mean())
x['social'] = x['social'].fillna(value=x['social'].mean())

print(x)
