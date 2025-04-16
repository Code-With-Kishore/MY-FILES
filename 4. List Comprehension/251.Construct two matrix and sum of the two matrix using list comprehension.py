# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:21:33 2024

@author: Admin
"""

x=[[int(input('Enter the m1 value:'))for i in range(3)]for j in range(3)]

y=[[int(input('Enter the m2 value:'))for i in range(3)]for j in range(3)]

z=[[x[i][j]+y[i][j]for i in range(3)]for j in range(3)]

print('matrix1',x)
print('matrix2',y)
print('sum of m1 and m2',z)
