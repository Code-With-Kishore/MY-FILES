# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 19:21:18 2025

@author: Admin
"""

import pandas as pd
import numpy as np
roll=[225213101+i for i in range(20)]
m=np.random.randint(50,100,(20,5),dtype=np.uint32)
x=pd.DataFrame(m,index=roll)
x.pop(0)
print('\nData\n',x)
