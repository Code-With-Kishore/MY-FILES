# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 04:24:55 2024

@author: Admin
"""

import csv
f=open('stud.csv')
x=csv.reader(f)
a=next(x)
b=next(x)
c=next(x)
d=next(x)
e=next(x)
print(a)
print(b)
print(c)
print(d)
print(e)