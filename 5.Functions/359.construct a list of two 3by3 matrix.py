# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 06:53:11 2024

@author: Admin
"""
import random
matrix=lambda n: [[random.randint(0,100)for i in range(n)]for j in range(n)]
n=int(input('Enter n value:'))
matrix1=matrix(n)
matrix2=matrix(n)
print('matrix1:',matrix1)
print('matrix2:',matrix2)