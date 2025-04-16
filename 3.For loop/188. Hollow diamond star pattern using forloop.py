# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 03:25:15 2024

@author: Admin
"""

n=int(input('Enter the no. of rows:'))

print(' '*n +'*')

for i in range(1,n):
    print(' '*(n-i) +'*' + ' ' * ((2*i)-1)+'*')

for j in range(0,n):
    print(' '*j+'*' + ' '*(2*(n-j)-1)+'*')
    
print(' '*n +'*')