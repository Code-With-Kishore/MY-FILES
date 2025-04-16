# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:06:38 2024

@author: Admin
"""

x=[[int(input('Enter the m1 value:'))for i in range(3)]for j in range(3)]

y=[[int(input('Enter the m2 value:'))for i in range(3)]for j in range(3)]

z=[[x[i][j]-y[i][j]for i in range(3)]for j in range(3)]

print('m1',x)
print('m2',y)
print('difference of 2 matrix',z)