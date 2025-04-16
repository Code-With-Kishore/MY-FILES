# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:26:58 2024

@author: Admin
"""
s1=input('Enter a string:')
s2=''
ln=len(s1)
d=ln-1
for i in range(d, -1, -1):
    s2+=s1[i]
print(s2)
