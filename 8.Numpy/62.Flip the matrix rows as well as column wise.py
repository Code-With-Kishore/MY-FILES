# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 11:43:29 2025

@author: Admin
"""

import numpy as np

rows = int(input('Enter row value:'))
cols = int(input('Enter column value:'))

matrix = np.random.randint(1, 100, (rows, cols))

print("Original Matrix:\n", matrix)

flipped_matrix = matrix[ ::-1 , ::-1]

print("\nFlipped Rows and Column Matrix:\n", flipped_matrix)