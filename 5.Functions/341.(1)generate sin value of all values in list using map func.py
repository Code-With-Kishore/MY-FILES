# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 05:29:13 2024

@author: Admin
"""

import random
import math
n=int(input('Enter n values:'))
a=[random.randint(1,100)for i in range(n)]
b=map(math.sin,a)
c=list(b)

print(a)
print(c)