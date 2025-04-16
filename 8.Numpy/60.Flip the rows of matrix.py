# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 19:38:49 2025

@author: Admin
"""

import numpy as np

rows = int(input('Enter row value:'))
cols = int(input('Enter column value:'))

matrix = np.random.randint(1, 100, (rows, cols))

print("Original Matrix:\n", matrix)

flipped_matrix = matrix[::-1]

print("\nFlipped Rows Matrix:\n", flipped_matrix)
