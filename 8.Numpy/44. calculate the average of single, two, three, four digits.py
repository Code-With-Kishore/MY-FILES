# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:53:46 2025

@author: Admin
"""

import numpy as np

n=int(input('Enter n value: '))

x=np.random.randint(0, 10000, n)

single=x[(x>=0) & (x<=9)]
two=x[(x>=10) & (x<=99)]
three=x[(x>=100) & (x<=999)]
four=x[(x>=1000) & (x<=9999)]

s1=sum(single)
s2=sum(two)
s3=sum(three)
s4=sum(four)

ln1=len(single)
ln2=len(two)
ln3=len(three)
ln4=len(four)

avg_single= s1/ln1 
avg_two= s2/ln2 
avg_three= s3/ln3 
avg_four= s4/ln4 

a= avg_single if ln1>0 else 0
b= avg_two if ln2>0 else 0
c= avg_three if ln3>0 else 0
d= avg_four if ln4>0 else 0

print('Average of Single Digits: ', a)
print('Average of Two Digits: ', b)
print('Average of Three Digits: ', c)
print('Average of Four Digits', d)
