# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 04:08:07 2024

@author: Admin
"""

d={}
n=int(input('Enter n times of stud data:'))
for i in range(n):
    a=input('Name:')
    b=int(input('age:'))
    c=input('location:')
    biodata=(a, b, c)
    rollno=int(input('Enter roll.no.:'))
    d[rollno]=biodata
print(d)