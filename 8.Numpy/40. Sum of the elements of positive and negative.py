# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:56:04 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
x=np.random.randint(-128, 127, n)

ap=x[x>=0]
an=x[x<0]

sum1=sum(ap)
sum2=sum(an)

print('sum of the elements of positive value: ',sum1)
print('sum of the elements of negative value: ',sum2)