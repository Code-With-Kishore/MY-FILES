# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:59:17 2025

@author: Admin
"""

import numpy as np

n=int(input('Enter n value: '))

x=np.random.randint(0, 10000, n)

single=x[(x>=0) & (x<=9)]
two=x[(x>=10) & (x<=99)]
three=x[(x>=100) & (x<=999)]
four=x[(x>=1000) & (x<=9999)]

print('Single Digits: ', single)
print('Two Digits: ', two)
print('Three Digits: ', three)
print('Four Digits', four)