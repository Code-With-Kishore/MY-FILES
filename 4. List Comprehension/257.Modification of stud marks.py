# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:24:41 2024

@author: Admin
"""
#Modified the mark of student if the mark is(35-39)it will is convert into 40.
n=int(input('Enter the no. of student:'))
mark=[int(input('Enter the original mark:')) for i in range(n)]
x=[40 if j>=35 and j<=39 else j for j in mark]
print('mark of student:', mark)
print('modified mark:', x)