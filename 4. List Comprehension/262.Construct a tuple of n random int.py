# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:20:43 2024

@author: Admin
"""

import random
n=int(input('Enter the n value:'))
x=[random.randint(1,100)for i in range(n)]
a=tuple(x)
print(a)
