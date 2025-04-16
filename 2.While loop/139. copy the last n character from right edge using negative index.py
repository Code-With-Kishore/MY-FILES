# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 22:42:15 2024

@author: Admin
"""
#copy the last n char from right edge using negative index.

s1=input('Enter a string:')
s2=''
ln=len(s1)
n=int(input('Enter a n value:'))
i=ln-n
while i<=ln:
    s2=s2+s1[-i]
    i=i+1
print(s2)