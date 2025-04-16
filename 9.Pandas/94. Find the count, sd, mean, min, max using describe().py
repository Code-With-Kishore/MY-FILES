# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 18:15:03 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))

s1=np.random.randint(1,10,n)

r=[225214201+i for i in range(n)]

x=pd.Series(data=s1, index=r)

print('\nSeries Data:\n',x)
print('\nDestribe val:\n',x.describe())