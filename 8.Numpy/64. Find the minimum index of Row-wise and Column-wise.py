# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 17:58:46 2025

@author: Admin
"""

import numpy as np

rows = int(input('Enter row value: '))  
cols = int(input('Enter column value: '))  

matrix = np.random.randint(1, 100, (rows, cols))  
print("Original Matrix:\n", matrix)

x = matrix.argmin()  # Lowest index value of matrix.
print("Index of Min Element in Matrix:", x)

y = matrix.argmin(0) # Lowest index value Column-Wise.
print("Column-wise Min Index:\n", y)

z = matrix.argmin(1) # Lowest index value Row-Wise.
print("Row-wise Min Index:\n", z)
