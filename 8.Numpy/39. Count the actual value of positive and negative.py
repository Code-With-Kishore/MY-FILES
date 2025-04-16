# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:33:33 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
x=np.random.randint(-128, 127, n)

ap=x[x>=0]
an=x[x<0]

ln1=len(ap)
ln2=len(an)

print('Length of positive value: ',ln1)
print('Length of negative value: ',ln2)

