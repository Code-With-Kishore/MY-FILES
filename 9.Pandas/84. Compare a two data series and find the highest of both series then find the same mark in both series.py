# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:37:50 2025

@author: Admin
"""

import random as rd
import pandas as pd

n = int(input('Enter n value: '))

end= [rd.randint(50, 100) for i in range(n)]
mis= [rd.randint(50, 100) for i in range(n)]
roll_numbers = [225214201 + i for i in range(n)]  
absent_stud = [225214201, 225214205, 225214207, 225214210]

s= pd.Series(data=mis, index=roll_numbers)
s2= pd.Series(data=end, index=roll_numbers)

print(s)
print(s2)

for j in absent_stud:  
    s[j] = pd.NA
    s2[j]=pd.NA
    
c=s.dropna()
c2=s2.dropna()

hmc=c>c2
hmc2=c2>c
sm=c==c2

sm1=c[sm]
hm1=c[hmc]
hm2=c2[hmc2]

print("highest mark of mid sem",hm1)
print("highest mark of end sem ",hm2)
print("same mark in both sem",sm1)