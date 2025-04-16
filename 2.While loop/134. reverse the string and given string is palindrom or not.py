# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 23:04:38 2024

@author: Admin
"""
#Reverse the string and check the given string is palindrom or not.

s1=input('Enter a string:')
s2=''
ln=len(s1)
i=ln-1
while i>=0:
    s2=s2+s1[i]
    i=i-1
print(s2)
if s1==s2:
    print('its a palindrom')
else:
    print('not a palindrom')
    
    