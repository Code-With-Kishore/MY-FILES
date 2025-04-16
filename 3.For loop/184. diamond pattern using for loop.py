# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 01:40:45 2024

@author: Admin
"""

n=5
for i in range(1, n):
    print(' '*(n-i) +'*'*((2*i)-1))

for j in range(0, n):
    print(' '*j+'*'*(2*(n-j)-1))