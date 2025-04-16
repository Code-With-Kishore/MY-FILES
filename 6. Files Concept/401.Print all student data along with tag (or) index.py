# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 04:49:00 2024

@author: Admin
"""

import csv
f=open('stud.csv')
x=csv.reader(f)
a=next(x)
for i in x:    
    print(a[0],i[0])
    print(a[1],i[1])
    print(a[2],i[2])
    print(a[3],i[3])
    print(a[4],i[4])
    print(a[5],i[5])
    print(a[6],i[6])
    print(a[7],i[7])
    print(a[8],i[8])
