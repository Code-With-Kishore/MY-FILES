# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:17:34 2024

@author: Admin
"""
#print the pattern.
n=int(input('Enter n value:'))
for i in range(1, n):
    print('*'*i)
for j in range(n, 0, -1):
    print('*'*j)