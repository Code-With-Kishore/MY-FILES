# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 16:47:06 2025

@author: Admin
"""

import pandas as pd
import numpy as np

roll=[225213101+i for i in range(20)]

sub = ['tamil', 'english', 'maths', 'science', 'social']

m=np.random.randint(0,100,(20,5),dtype=np.uint8)

x=pd.DataFrame(m,index=roll,columns=sub)

print(x)

f2=x.loc[:,'tamil':'english']

print("\nFirst 2 columns:\n", f2)

m1=x.loc[:,'english':'science']

print("\nmiddle three columns:\n", m1)

l2=x.loc[:,'science':'social']

print("\nlast 2 columns:\n",l2)