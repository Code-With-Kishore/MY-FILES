# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 00:13:56 2024

@author: Admin
"""
#Extract n character from s1.
s1=input('Enter a string:')
s2=' '
n=int(input('Enter a value:'))
i=0
while i<=n:
    s2=s2+s1[i]
    i=i+1
    print(s2)