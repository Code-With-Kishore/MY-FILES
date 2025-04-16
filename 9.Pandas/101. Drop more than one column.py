# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 18:53:00 2025

@author: Admin
"""

import pandas as pd
import numpy as np
roll=[225213101+i for i in range(20)]
sub = ['tamil', 'english', 'maths', 'science', 'social']
m=np.random.randint(50,100,(20,5),dtype=np.uint32)
x=pd.DataFrame(m,index=roll,columns=sub)
print('\nData\n',x)

d=x.drop(['tamil', 'science'], axis=1)
print('\nDelete more than 1 Column\n',d)