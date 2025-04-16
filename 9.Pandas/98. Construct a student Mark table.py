# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 18:54:47 2025

@author: Admin
"""

import pandas as pd
import numpy as np
r=int(input('Enter Row value: '))
c=int(input('Enter Column value: '))
s=np.random.randint(50,100,(r,c), dtype=np.uint8)
x=pd.DataFrame(s)
print(x)