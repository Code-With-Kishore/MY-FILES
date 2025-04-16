# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 17:41:33 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))

s1=np.random.randint(1,10,n)

r=[225214201+i for i in range(n)]

x=pd.Series(data=s1, index=r)

print('\nSeries Data:\n',x)
print('\nSum of Series Data:\n',x.sum())
print('\nProduct of Series Data:\n',x.product())
print('\nMean val of Series Data:\n',x.mean())
print('\nMedian val of Series Data:\n',x.median())
print('\nMode val of Series Data:\n',x.mode())
print('\nMax of Series Data:\n',x.max())
print('\nMin of Series Data:\n',x.min())