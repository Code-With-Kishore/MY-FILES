# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 00:06:19 2024

@author: Admin
"""
#Extract a string.
s1=input('Enter a string:')
s2=' '
ln=len(s1)
i=0
while i<=ln-1:
    s2=s2+(s1[i])
    i=i+1
    print(s2)
    