# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 11:01:30 2025

@author: Admin
"""

import random as rd
import pandas as pd

n = int(input('Enter n value: '))

data = [rd.randint(1, 100) for i in range(n)]

roll_numbers = [225214201 + i for i in range(n)]  

absent_stud = [225214210, 225214215, 225214220, 225214225]

s = pd.Series(data, index=roll_numbers)

for j in absent_stud:  
    s[j] = pd.NA

first_ten = s.loc[225214201:225214210]
middle_five=s.loc[225214211:225214215]
last_ten=s.loc[225214216:225214225]
reverse=s.loc[::-1]

print('\nFirst Ten lines of rows:\n', first_ten)
print('\nMiddle Five lines of rows:\n', middle_five)
print('\nLast Ten lines of rows:\n',last_ten)
print('\nReverse the entire series:\n',reverse)