# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:56:40 2025

@author: Admin
"""

import numpy as np
import pandas as pd
n=int(input('Enter n value: '))
x=np.random.randint(0,1000,n)
y=pd.Series(x)
print(y)
