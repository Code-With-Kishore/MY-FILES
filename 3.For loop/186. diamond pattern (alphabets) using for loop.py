# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:19:16 2024

@author: Admin
"""

n=int(input('Enter n value:'))
for i in range(1,n):
    print(' '*(n-i), end="")
    for j in range((2*i)-1):
        print(chr(97+j), end="")
    print()

for i in range(0,n):
    print(' '*i, end="")
    for j in range((2*(n-i)-1)):
        print(chr(97+j), end="")
    print()
        
