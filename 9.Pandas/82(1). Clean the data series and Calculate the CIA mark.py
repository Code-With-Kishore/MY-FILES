# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 10:26:28 2025

@author: Admin
"""

import numpy as np
import pandas as pd
n =int(input('Enter n value: '))
m1=np.random.randint(30,100,n)
m2=np.random.randint(30,100,n)
seminar=np.random.randint(30,100,n)
atd=np.random.randint(30,100,n)
roll_no= [225214201 + i for i in range(n)]
missing_data= [225214201, 225214205, 225214207, 225214210,225214229,225214249]
m1s= pd.Series(m1,index=roll_no)
m2s= pd.Series(m2,index=roll_no)
semi_s= pd.Series(seminar,index=roll_no)
atd_s= pd.Series(atd,index=roll_no)
for j in missing_data:  
    m1s[j] = pd.NA
    m2s[j] = pd.NA
    semi_s[j] = pd.NA
    atd_s[j] = pd.NA
m1d=m1s.dropna()
m2d=m2s.dropna()
semi_d=semi_s.dropna()
atd_d=atd_s.dropna()
tm1=(m1d/100)*15
tm2=(m2d/100)*15
sm=(semi_d/100)*5
am=(atd_d/100)*5
total_CIA_mark=tm1+tm2+sm+am
print(m1s)
print(m2s)
print(semi_s)
print(atd_s)
print(total_CIA_mark)