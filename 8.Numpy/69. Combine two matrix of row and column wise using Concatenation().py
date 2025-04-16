# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:39:10 2025

@author: Admin
"""

import numpy as np
rows=int(input('Enter row value: '))
cols = int(input('Enter column value: '))  

matrix1 = np.random.randint(0, 500, (rows, cols)) 
matrix2= np.random.randint(500, 1000, (rows, cols)) 

x=np.concatenate([matrix1, matrix2], axis=0) #Column wise Concatenate.
y=np.concatenate([matrix1, matrix2], axis=1) #Row wise Concatenate.

print('Matrix1:\n',matrix1)
print('Matrix2:\n',matrix2)
print('Concatenate Column-Wise:\n', x)
print('Concatenate Row-Wise:\n', y)