# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:06:31 2024

@author: Admin
"""

s=input('Enter a string:')
x=0
y=0
for i in s:
    if i in 'aeiou':
        x=x+1
    else:
        y=y+1
print('no. of vowels:',x)
print('no. of non-vowels:',y)