# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 18:06:07 2025

@author: Admin
"""

import random as rd
import pandas as pd

n = int(input('Enter n value: '))

term1 = [rd.randint(50, 100) for i in range(n)]
term2 = [rd.randint(50, 100) for i in range(n)]

roll_numbers = [225214201 + i for i in range(n)]  

absent_stud = [225214201, 225214205, 225214207, 225214210]

x = pd.Series(data=term1, index=roll_numbers)

for j in absent_stud:  
    x[j] = pd.NA
    
y = pd.Series(data=term2, index=roll_numbers)
z = x+y
    
print("\nTerm 1 Marks:\n", x)
print("\nTerm 2 Marks:\n", y)
print("\nTotal Marks (Term 1 + Term 2):\n", z)
    

