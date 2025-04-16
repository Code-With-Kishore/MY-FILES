# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 18:01:58 2025

@author: Admin
"""

import numpy as np

rows = int(input('Enter rows value: '))
col = int(input('Enter column value: '))
m = np.random.randint(-100, 100, (rows, col))

x = m[:2: , :1:]   
y = m[2:3: , 1:4: ]  
z = m[-2: :  , -1: :]   

# Display results
print("\nOriginal Matrix:\n", m)
print("\nFirst 2 Rows and First Column Extraction:\n", x)
print("\nMiddle 1 Rows and Middle 3 Column Extraction:\n", y)
print("\nLast 2 Rows and Last one column Extraction:\n", z)