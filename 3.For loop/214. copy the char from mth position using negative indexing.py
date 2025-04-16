# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 06:07:28 2024

@author: Admin
"""

s1=input('Enter a string:')
s2=' '
ln=len(s1)
m=int(input('Enter the position:'))
s2=s1[-m:-ln:-1]+s1[0]
print(s2)