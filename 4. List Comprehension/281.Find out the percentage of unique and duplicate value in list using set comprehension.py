# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:14:35 2024

@author: Admin
"""
import random
a=set()
n=int(input('Enter n value:'))
x=[random.randint(0,1000) for i in range(n)]
unique={i for i in x}
unique_value=len(unique)
total_value=len(x)

unique_percent=(unique_value/total_value*100)
duplicate_percent=(100-unique_percent)

print('Unique Value is:',unique)
print('Percentage of unique value is:',unique_percent)
print('Percentage of duplicate value is:',duplicate_percent)


