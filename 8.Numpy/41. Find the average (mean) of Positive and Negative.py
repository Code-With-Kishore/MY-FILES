# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:02:10 2025

@author: Admin
"""


import numpy as np
n=int(input('Enter n value: '))
x=np.random.randint(-128, 127, n)

ap=x[x>=0]
an=x[x<0]

sum1=sum(ap)
sum2=sum(an)

ln1=len(ap)
ln2=len(an)

avg_positive=sum1/ln1
avg_negative=sum2/ln2

print('Sum of Positive:', sum1)
print('Sum of Negative:', sum2)
print('Length of Positive: ', ln1)
print('Length of Negative: ', ln2)
print('Average of Positive: ',avg_positive)
print('Average of Negative: ',avg_negative)
