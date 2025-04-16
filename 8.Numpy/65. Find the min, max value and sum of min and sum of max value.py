# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 18:19:56 2025

@author: Admin
"""

import numpy as np

rows = int(input('Enter row value: '))  
cols = int(input('Enter column value: '))  

matrix = np.random.randint(1, 100, (rows, cols))  
print("Original Matrix:\n", matrix)

x = matrix.min()  
print("Min Element in Matrix:", x)

y = matrix.min(0) 
print("Column-wise Min:", y)

z = matrix.min(1) 
print("Row-wise Min:", z)

minimum_col=np.sum(y)
print("Sum of Min Column-wise :", minimum_col)
minimum_row=np.sum(z)
print("Sum of Min Row-wise :", minimum_row)

i = matrix.max()  
print("Max Element in Matrix:", i)

j = matrix.max(0) 
print("Column-wise Max:", j)

k = matrix.max(1) 
print("Row-wise Max:", k)

max_row=np.sum(j)
print("Sum of Max Row-wise :", max_row)
max_col=np.sum(k)
print("Sum of Max Column-wise :", max_col)

