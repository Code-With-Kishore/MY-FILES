# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:55:17 2024
#copy the last n character.
@author: Admin
"""
s1=input('Enter a string:')
s2=''
ln=len(s1)
n=int(input('Enter a n value:'))
i=ln-n
while i<=ln-1:
    s2=s2+s1[i]
    i=i+1
print(s2)