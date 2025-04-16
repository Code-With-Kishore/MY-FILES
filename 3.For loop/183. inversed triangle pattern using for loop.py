# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:09:41 2024

@author: Admin
"""
n=int(input('Enter a no. of rows:'))
for i in range(0, n):
    print(' '*i+'*'*(2*(n-i)-1))