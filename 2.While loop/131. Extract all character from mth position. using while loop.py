# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 01:48:38 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=' '
m=int(input('Enter a value:'))
ln=len(s1)
i=m
while i<=ln-1:
    s2=s2+s1[i]
    i=i+1
print(s2)

    
