# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 18:21:01 2025

@author: Admin
"""

import pandas as pd
import numpy as np
n=int(input('Enter n value: '))
s=np.random.randint(0,50,n)
x=pd.DataFrame(s)
print(x)