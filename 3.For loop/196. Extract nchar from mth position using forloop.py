# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:48:33 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=''
n=int(input('Enter a no.of char:'))
m=int(input('Enter no. of position:'))
ln=len(s1)
for i in range(m, m+n):
    s2+=s1[i]
print(s2)
