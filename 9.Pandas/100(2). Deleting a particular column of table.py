# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:25:22 2025

@author: Admin
"""

import pandas as pd
import numpy as np
roll=[225213101+i for i in range(20)]
sub = ['tamil', 'english', 'maths', 'science', 'social']
m=np.random.randint(50,100,(20,5),dtype=np.uint32)
x=pd.DataFrame(m,index=roll,columns=sub)
print('\nData\n',x)
del x['tamil']
del x['social']
print('\nDelete a Particular Column\n',x)