# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:26:20 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
x=np.random.randint(0, 100, n)

mean_val=np.mean(x) #Sum of value divided by length
median_val=np.median(x) #Middle value or Average of two middle value it depents on the list value is odd or even.
var=np.var(x) #Sum of square differnce divided by length.
std_dev=np.std(x) #Measure the spread out numbers are from the mean value.

print('Random Generate Number:', x)
print('Mean value: ', mean_val)
print('Median value: ', median_val)
print('Varience:', var)
print('Standard deviation:', std_dev)