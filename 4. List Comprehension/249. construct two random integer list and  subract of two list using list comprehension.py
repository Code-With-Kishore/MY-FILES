# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 07:07:32 2024

@author: Admin
"""

import random
n=int(input('Enter the integer value:'))
x=[random.randint(1,101)for i in range(n)]
y=[random.randint(1,101)for j in range(n)]
z=[x[k]-y[k] for k in range(n)]

print('generated list of x is:',x)
print('generated list of y is:',y)
print('Subraction of x and y value is',z)