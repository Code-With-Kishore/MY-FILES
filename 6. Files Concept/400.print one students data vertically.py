# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 04:34:50 2024

@author: Admin
"""

import csv
f=open('stud.csv')
x=csv.reader(f)
a=next(x)
b=next(x)
print(a[0],b[0])
print(a[1],b[1])
print(a[2],b[2])
print(a[3],b[3])
print(a[4],b[4])
print(a[5],b[5])
print(a[6],b[6])
print(a[7],b[7])
print(a[8],b[8])
print((a[9],b[9]))