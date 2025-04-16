# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 18:50:43 2025

@author: Admin
"""

import numpy as np
import pandas as pd

n=int(input('Enter n value: '))
nlar=int(input('Enter N largest value: '))
nsma=int(input('Enter N smallest value: '))

s1=np.random.randint(1,100,n)

r=[225214201+i for i in range(n)]

x=pd.Series(data=s1, index=r)

l=x.nlargest(nlar)
s=x.nsmallest(nsma)

print('\nSeries Data:\n', x)
print('\nNLargest data:\n', l)
print('\nNSmallest data:\n',s)
