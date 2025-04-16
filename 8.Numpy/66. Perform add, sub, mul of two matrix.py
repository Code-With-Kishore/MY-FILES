# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 19:06:08 2025

@author: Admin
"""

import numpy as np
rows=int(input('Enter row value: '))
cols = int(input('Enter column value: '))  

matrix1 = np.random.randint(0, 500, (rows, cols)) 
matrix2= np.random.randint(500, 1000, (rows, cols)) 

a=np.add(matrix1, matrix2)
b=np.subtract(matrix1, matrix2)
c=np.dot(matrix1, matrix2)

print('Matrix 1:\n', matrix1)
print('Matrix 2:\n', matrix2)
print('Addition of two Matrix:\n', a)
print('Subraction of two Matrix:\n', b)
print('Multiplication of two Matrix:\n', c)
