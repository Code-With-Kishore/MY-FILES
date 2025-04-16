# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 10:48:42 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))

s1=np.random.randint(1,10,n)
s2=np.random.randint(1,10,n)
r=[225214201+i for i in range(n)]

x=pd.Series(data=s1, index=r)
y=pd.Series(data=s2, index=r)

z=x.isin(y)

print('\nSeries 1 Data:\n', x)
print('\nSeries 2 Data:\n', y)
print('\nCheck s1 data available in s2:\n',z)