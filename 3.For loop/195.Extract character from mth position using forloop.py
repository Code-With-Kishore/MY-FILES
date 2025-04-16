# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:38:34 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=''
m=int(input('Enter no. of position:'))
ln=len(s1)
for i in range(m, ln):
    s2+=s1[i]
print(s2)
