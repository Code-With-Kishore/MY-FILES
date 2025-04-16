# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 06:56:50 2024

@author: Admin
"""
import random
matrix=lambda n: [[random.randint(0,100)for i in range(n)]for j in range(n)]
n=int(input('Enter n value:'))
matrix1=matrix(n)
matrix2=matrix(n)
add=lambda matrix1,matrix2: matrix1+matrix2
total=[[matrix1[i][j]+matrix2[i][j] for i in range(n)]for j in range(n)]
print('matrix1 is:',matrix1)
print('matrix2 is:',matrix2)
print('sum of two matrix is:',total)