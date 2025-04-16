# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 08:08:30 2024

@author: Admin
"""

a=input('Enter a string:')
ln=len(a)
x=0
y=0
i=0
while i<=ln-1:
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        x=x+1
    else:
        y=y+1
    i=i+1
print('vowel:',x)
print('non-vowel:',y)
 