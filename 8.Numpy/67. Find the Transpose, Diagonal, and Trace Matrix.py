# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 10:41:49 2025

@author: Admin
"""

import numpy as np
rows=int(input('Enter row value:'))
cols = int(input('Enter column value: '))  

matrix = np.random.randint(0, 100, (rows, cols)) 

x=matrix.transpose() 
y=matrix.diagonal() #Row index is equal to column index.
z=matrix.trace() #Sum of a diagonal matrix.

print('Random Generated matrix:\n',matrix)
print('Transpose of matrix:\n', x)
print('Diagonal matrix:\n',y)
print('Trace matrix:\n',z)
