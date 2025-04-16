# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:35:59 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=''
ln=len(s1)
d=ln-1
for i in range(d, -1, -1):
    s2=s2+s1[i]
print(s2)

# Now check the given string is palindrom or not.

if s2==s1:
    print('your input of',s1,'is palindrom')
else:
    print('your input of',s1,'is not a palindrom')