# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 05:36:37 2024

@author: Admin
"""

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

ln=len(lst)
i=0
while i<=ln-1:
    print(lst[i])
    i=i+1