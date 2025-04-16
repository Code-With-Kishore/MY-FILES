# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 06:43:15 2024

@author: Admin
"""
#print the no. 1000 to 3000 is leapyear or not using for loop.
for i in range(1000, 3000):
    if i%4:
        print(i, 'is not a leapyear')
    else:
        print(i, 'is a leapyear')