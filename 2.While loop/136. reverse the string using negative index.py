# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:59:59 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=''
ln=len(s1)
i=1
while i<=ln:
    s2=s2+s1[-i]
    i=i+1
print(s2)