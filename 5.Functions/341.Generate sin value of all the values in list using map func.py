# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 05:31:01 2024

@author: Admin
"""

import random
import math
def sin_val(x):
    y=math.sin(x)
    return y
#main
n=int(input('Enter the n value:'))
a=[random.randint(1,100)for i in range(n)]
b=map(sin_val,a)
c=list(b)
print(a)
print(c)