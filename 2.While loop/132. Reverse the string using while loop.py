# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 07:31:42 2024

@author: Admin
"""

s1=input('Enter a string:') #linsoft academy
s2=''
ln=len(s1) #14
i=ln-1
while i>=0:
    s2=s2+s1[i]
    i=i-1
print(s2)