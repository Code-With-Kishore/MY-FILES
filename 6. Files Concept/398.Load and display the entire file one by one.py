# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:38:02 2024

@author: Admin
"""

import csv
f=open("stud.csv")
x=csv.reader(f)

for i in x:
    print(i)