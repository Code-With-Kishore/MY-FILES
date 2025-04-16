# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 07:22:35 2024

@author: Admin
"""
n=int(input('Enter a no. of rows:'))
for i in range(1, n):
    print('-'*(n-i)+'*'*i)
for i in range(0, n):
    print('-'*i+'*'*(n-i))
    