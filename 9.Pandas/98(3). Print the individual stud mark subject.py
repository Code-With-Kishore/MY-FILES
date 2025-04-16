# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 10:16:17 2025

@author: Admin
"""

import pandas as pd
import numpy as np
sub=['tamil','english','maths','science','social']
roll=[225213101+i for i in range(20)]
m=np.random.randint(0,100,(20,5),dtype=np.uint8)
x=pd.DataFrame(m,index=roll,columns=sub)
print(x)

t=x[['tamil']]
e=x[['english']]
m=x[['maths']]
s=x[['science']]
h=x[['social']]

print(t)
print(e)
print(m)
print(s)
print(h)