# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 09:56:48 2025

@author: Admin
"""

import pandas as pd
import numpy as np
roll=[225213101+i for i in range(20)]
m=np.random.randint(50,100,(20,5),dtype=np.uint32)
x=pd.DataFrame(m,index=roll)

h=x.head()
t=x.tail()
d=x.describe()

print('\nData\n',x)
print('\nFirst few lines of Data\n',h)
print('\nLast few lines of Data\n',t)
print('\nDescribe the overall Data\n',d)
