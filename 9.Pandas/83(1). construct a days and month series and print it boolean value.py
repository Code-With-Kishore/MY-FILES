# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:30:04 2025

@author: Admin
"""

import pandas as pd
import random as rd
days=[rd.randint(28,31)for i in range(12)]
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec']
s=pd.Series(days,index=months)
print(s)

months_31 =s == 31
months_30 =s == 30
months_29 = s== 29
print("\nMonths with 31 days:\n", months_31)
print("\nMonths with 30 days:\n", months_30)
print("\nMonths with 29 days:\n", months_29)
