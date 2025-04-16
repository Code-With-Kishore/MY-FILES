# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 09:15:10 2024

@author: Admin
"""
#Construct a list of n students biodata.
lst=[]
n=int(input('Enter a number of students:'))
i=0
while i<n:
    lst2=[]
    a=input('Enter the Name:')
    b=int(input('Enter the Age:'))
    c=input('Enter the gender:')
    d=input('Enter the qualification:')
    e=input('Enter the location:')
    x=[a, b, c, d, e]
    lst.append(x)
    i=i+1
print(lst)

