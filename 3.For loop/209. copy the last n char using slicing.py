# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 06:53:34 2024

@author: Admin
"""
s1=input('Enter a string:')
s2=' '
ln=len(s1)
n=int(input('Enter a n value:'))
x=ln-n
s2=s1[x:ln]
print(s2)
