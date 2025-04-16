# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:39:46 2024

@author: Admin
"""

s1=input('Enter the string:')
s2=''
ln=-len(s1)-1
for i in range(-1,ln,-1):
    s2+=s1[i]
print(s2)
