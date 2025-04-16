# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 17:48:15 2025

@author: Admin
"""

import random as rd
import pandas as pd

n = int(input('Enter n value: '))

term1 = [rd.randint(50, 100) for i in range(n)]
term2 = [rd.randint(50, 100) for i in range(n)]

rollnum = [225214201 + i for i in range(n)]

x = pd.Series(data=term1, index=rollnum)
y = pd.Series(data=term2, index=rollnum)

s = x + y

print("\nTerm 1 Marks:\n", x)
print("\nTerm 2 Marks:\n", y)
print("\nTotal Marks (Term 1 + Term 2):\n", s)

