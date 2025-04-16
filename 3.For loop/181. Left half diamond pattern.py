# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 09:23:46 2024

@author: Admin
"""
n=int(input('Enter a no. of rows:'))
for i in range(1, n):
    print(' '*(n-i)+'*'*i)
for j in range(0, n):
    print(' '*j+'*'*(n-j))
    