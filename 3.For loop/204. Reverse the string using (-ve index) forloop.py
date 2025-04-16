# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 05:16:55 2024

@author: Admin
"""

s1=input('Enter the string:')
s2=''
ln=len(s1)
for i in range(1, ln+1, 1):
    s2+=s1[-i]
print(s2)