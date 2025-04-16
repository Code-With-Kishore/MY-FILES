# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:01:07 2024

@author: Admin
"""

s=input('Enter a string:')
for i in s:
    if i not in 'aeiou':
        print(i)