# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 19:13:00 2025

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

first_ten = s[ :10]
middle_five=s[10:15]
last_ten=s[-10: ]

print('\nFirst Ten lines of rows:\n', first_ten)
print('\nMiddle Five lines of rows:\n', middle_five)
print('\nLast Ten lines of rows:\n',last_ten)