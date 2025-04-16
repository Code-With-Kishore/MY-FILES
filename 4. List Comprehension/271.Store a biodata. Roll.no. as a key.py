# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 06:24:43 2024

@author: Admin
"""

a=input('Enter Name:')
b=int(input('Enter Age:'))
c=input('Enter qualification:')
d=input('Enter Gender:')
e=input('Enter Location:')

biodata=[a,b,c,d,e]

d={}
roll_number=int(input('Enter Roll.no.:'))
d[roll_number]=biodata
print(d)