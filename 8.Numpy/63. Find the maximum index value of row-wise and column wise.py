# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 14:47:45 2025

@author: Admin
"""

import numpy as np

rows = int(input('Enter row value: '))  
cols = int(input('Enter column value: '))  

matrix = np.random.randint(1, 100, (rows, cols))  
print("Original Matrix:\n", matrix)

x = matrix.argmax()  # Highest index value of matrix.
print("Index of Max Element in Matrix:", x)

y = matrix.argmax(0) # Highest index value Column-Wise.
print("Column-wise Maximum Index:\n", y)

z = matrix.argmax(1) # Highest index value Row-Wise.
print("Row-wise Maximum Index:\n", z)

