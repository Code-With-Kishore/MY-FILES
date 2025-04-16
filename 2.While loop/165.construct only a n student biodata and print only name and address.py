# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 06:08:34 2024

@author: Admin
"""

s=[]
n=int(input('Enter n student value:'))
i=0
while i<n:
    a=input('Enter Name:')
    b=int(input('Enter Age:'))
    c=input('Enter the Location:')
    x=(a, b, c)
    s.append(x)
    i=i+1

ln=len(s)
i=0
while i<=ln-1:
    print(s[i][0])
    print(s[i][1])
    i=i+1