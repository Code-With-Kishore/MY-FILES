# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 06:10:21 2024

@author: Admin
"""
import random
x=[random.randint(-1,10000) for i in range(100)]
a=[i for i in x if i>=0 and i<=9]
b=[i for i in x if i>=10 and i<=99]
c=[i for i in x if i>=100 and i<=999]
d=[i for i in x if i>=1000 and i<=9999]

print(x)
print('single digits are:',a)
print('two digits are:',b)
print('three digits are',c)
print('four digits are:',d)
