# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 06:50:50 2024

@author: Admin
"""
n=int(input("Enter n value:"))
for i in range(1,n):
    for j in range(n-i):
        print(' ', end="")
    for k in range (1,2*i):
        print(k, end='')
    print()
        
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end="")
    for k in range(1,2*i):
        print(k , end="")
    print()