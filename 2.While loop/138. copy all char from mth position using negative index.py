# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 05:34:34 2024

@author: Admin
"""
#Copy all the character from mth position using negative index.

s1=input('Enter a string:')
s2=''
ln=-len(s1)
m=int(input('Enter a position:'))
i=1
while i<=m:
    s2=s2+s1[-i]
    i=i+1
print(s2)