# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:17:58 2024

@author: Admin
"""

import random
n=int(input('Enter n value:'))
x=[random.randint(0,100)for i in range(n)]
a=set(x)
print(a)