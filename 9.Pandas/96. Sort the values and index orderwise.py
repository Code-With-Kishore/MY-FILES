# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 17:53:21 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))

s1=np.random.randint(1,50,n)

r=[225214201+i for i in range(n)]

x=pd.Series(data=s1, index=r)

y=x.sort_values(ascending=True) #Sort values Order-wise.
z=x.sort_index(ascending=True) #Sort index Order-wise.

print('\nSeries of Data :\n', x)
print('\nSort the series data order-wise :\n',y)
print('\nSort the series data (index) order-wise :\n',z)