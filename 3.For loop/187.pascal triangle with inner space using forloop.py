# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:06:31 2024

@author: Admin
"""

n=int(input('Enter a no.of rows:'))
print(' '*5 +'*')

for i in range(1,n):
    print(' '*(n-i) +'*' + ' ' * ((2*i)-1)+'*')
   
print('* ' *(n+1))

