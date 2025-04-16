# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 18:38:48 2025

@author: Admin
"""

import numpy as np

rows = int(input('Enter rows value: '))
col = int(input('Enter column value: '))
m = np.random.randint(-100, 100, (rows, col))

first_2 = m[:2]   
middle_1 = m[2:3]  
last_2 = m[-2:]   

# Display results
print("\nOriginal Matrix:\n", m)
print("\nFirst 2 Rows:\n", first_2)
print("\nMiddle 1 Rows:\n", middle_1)
print("\nLast 2 Rows:\n", last_2)


