# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 07:07:18 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=' '
ln=len(s1)-1
s2=s1[::-1]
print(s2)

if s1==s2:
    print('its a palindrom')
else:
    print('its not a palindrom')
    