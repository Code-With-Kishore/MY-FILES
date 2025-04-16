# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 18:32:45 2025

@author: Admin
"""

import random as rd
import pandas as pd
n = int(input('Enter n value: '))
marks= [rd.randint(0, 100) for i in range(n)]
roll_numbers = [225214201 + i for i in range(n)]  
absent_stud = [225214201, 225214205, 225214207, 225214210]
s= pd.Series(marks, index=roll_numbers)
for j in absent_stud:  
    s[j] = pd.NA
s1=s.dropna()

below_30=s1[s1<=30]
ab_30=s1[(s1>=31)&(s1<=60)]
ab_60=s1[(s1>=61)&(s1<=80)]
ab_80=s1[s1>=81]

print("full series",s)
print("\nstuds marks below 30\n",below_30)
print("\nstuds marks 30to60 \n",ab_30)
print("\nsuds marks 60to80 \n",ab_60)
print("\nstuds marks 80to100 \n",ab_80)