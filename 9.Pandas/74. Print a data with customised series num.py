# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 10:52:49 2025

@author: Admin
"""

import random as rd
import pandas as pd
n=int(input('Enter n Value: '))
marks=[rd.randint(50,100)for i in range(n)]
roll_no=[1,2,3,4,5,6,7,8,9,10]
s=pd.Series(data=marks,index=roll_no)
print(marks)
print(roll_no)
print(s)