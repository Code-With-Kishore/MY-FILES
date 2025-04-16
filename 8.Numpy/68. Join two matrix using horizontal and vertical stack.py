# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:18:46 2025

@author: Admin
"""

import numpy as np
rows=int(input('Enter row value: '))
cols = int(input('Enter column value: '))  

matrix1 = np.random.randint(0, 500, (rows, cols)) 
matrix2= np.random.randint(500, 1000, (rows, cols)) 

x=np.hstack((matrix1, matrix2))
y=np.vstack((matrix1, matrix2))

print('Matrix1:\n',matrix1)
print('Matrix2:\n',matrix2)
print('Matrix join Horizontal stack:\n', x)
print('Matrix join Vertical stack:\n', y)
