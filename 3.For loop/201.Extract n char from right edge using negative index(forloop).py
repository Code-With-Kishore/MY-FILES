# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:08:36 2024

@author: Admin
"""

s1=input('Enter the string:')
s2=''
n=int(input('Enter n value:'))
for i in range(1,n,1):
    s2+=s1[-i]
print(s2)
