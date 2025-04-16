# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 01:05:24 2024

@author: Admin
"""

s1=input('Enter the string:')
s2=''
m=int(input('Enter mth position value:'))
ln=len(s1)
for i in range(m, ln+1):
    s2+=s1[-i]
print(s2)