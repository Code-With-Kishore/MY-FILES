# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 06:04:13 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=' '
n=int(input('Enter n value:'))
s2=s1[-1:-n:-1]
print(s2)