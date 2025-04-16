# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 10:52:40 2025

@author: Admin
"""

import pandas as pd
import numpy as np
sub=['tamil','english','maths','science','social']
roll=[225213101+i for i in range(20)]
m=np.random.randint(0,100,(20,5),dtype=np.uint8)
x=pd.DataFrame(m,index=roll,columns=sub)
print(x)
a=x[:5]
print("\nFirst 5 rows:\n", a)
m10=x[5:15]
print("\nmiddle 10 rows:\n", m10)
l5=x[-5:]
print("\nlast 5 rows:\n", a)