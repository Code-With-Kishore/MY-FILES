# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 18:08:59 2025

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

print("\nFull Series:\n", s)

print("\nthe Series empty:", s.empty)

print("the Series contain NaN values:", s.hasnans)

print("Total number of elements in Series:", len(s))

print("Total non-NA values:", s.count())

print("Total NA values:", len(s) - s.count())


