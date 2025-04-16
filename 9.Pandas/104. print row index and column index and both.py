# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 10:13:24 2025

@author: Admin
"""

import pandas as pd
import numpy as np
roll=[225213101+i for i in range(20)]
m=np.random.randint(50,100,(20,5),dtype=np.uint32)
x=pd.DataFrame(m,index=roll)

r_index=x.axes[0]
c_index=x.axes[1]
both = x.axes

print('\nData\n',x)
print('\nRow index\n',r_index)
print('\nColumn index\n',c_index)
print('\nBoth Row and column index\n',both)
