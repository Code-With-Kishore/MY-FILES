# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 18:34:41 2025

@author: Admin
"""
import numpy as np
import pandas as pd
n=int(input('Enter n value: '))
x=pd.Series(data=np.random.randint(0, 100, n))
print(x)