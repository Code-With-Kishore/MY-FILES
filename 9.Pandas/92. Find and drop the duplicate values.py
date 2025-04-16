# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 19:22:04 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))

s1=np.random.randint(1,10,n)

r=[225214201+i for i in range(n)]

x=pd.Series(data=s1, index=r)

d1=x.duplicated()
d2=x.drop_duplicates()

print('\nSeries Data:\n', x)
print('\nDuplicate data (Boolean Value):\n', d1)
print('\nDuplicate data (Actual Value):\n', x[d1])
print('\nDrop Duplicate data:\n',d2)


