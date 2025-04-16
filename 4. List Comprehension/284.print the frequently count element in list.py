# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 05:27:09 2024

@author: Admin
"""

import random
n=int(input('Enter n value:'))
a=[random.randint(0,1000) for i in range(n)]
x=set(a)
for i in x:
    y=a.count(i)
    print(i, y)