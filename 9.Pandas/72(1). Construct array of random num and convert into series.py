# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 18:11:50 2025

@author: Admin
"""

import numpy as np
import pandas as pd
import random
n=int(input('Enter n value: '))
x=[random.randint(0, 100)for i in range(n)]
y=np.array(x)
z=pd.Series(y)
print(z)