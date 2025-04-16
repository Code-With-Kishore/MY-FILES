# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 05:15:01 2024

@author: Admin
"""
#Reverse the string using negative indexing.
s1=input('Enter a string:')
s2=' '
ln=len(s1)
s2=s1[-1:-ln:-1]+s1[0]
print(s2)

