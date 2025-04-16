# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 05:12:27 2024

@author: Admin
"""
# Extract n character from right edge using negative indexing.

s1=input('Enter a string:')
s2=''
ln=-len(s1)
n=int(input('Enter a n value:'))
i=1
while i<=n:
    s2=s2+s1[-i]
    i=i+1
print(s2)