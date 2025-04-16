# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 01:10:33 2024

@author: Admin
"""

s1=input('Enter the string:')
s2=''
n=int(input('Enter n value:'))
ln=len(s1)
for i in range(ln-n, ln+1):
    s2+=s1[-i]
print(s2)