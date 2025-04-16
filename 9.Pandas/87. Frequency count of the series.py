# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 19:09:28 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))

d=np.random.randint(1,10,n)
r=[225214201+i for i in range(n)]

x=pd.Series(data=d, index=r, dtype='uint64')

print('\nSeries of Data:\n', x)
print('\nCount the Frequency of each data:\n',x.value_counts())