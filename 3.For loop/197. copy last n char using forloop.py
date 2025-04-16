# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:16:24 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=''
n=int(input('Enter a no.of char:'))
ln=len(s1)
d=ln-n
for i in range(d, ln):
    s2+=s1[i]
print(s2)
