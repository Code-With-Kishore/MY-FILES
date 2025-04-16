# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 18:40:39 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))

s1=np.random.randint(1,50,n)

r=[225214201+i for i in range(n)]

x=pd.Series(data=s1, index=r)

y=x.unique()
z=x.nunique()
c=x.value_counts()

print('\nSeries Data:\n',x)
print('\nUnique value of Series Data:\n',y)
print('\nTotal count of Unique values:\n',z)
print('\ncount of Unique values:\n',c)
