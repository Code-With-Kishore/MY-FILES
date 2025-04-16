# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 06:05:10 2024

@author: Admin
"""

import random
x=lambda n: [random.randint(1,1000)for i in range(n)]
n=int(input('Enter n value:'))
y=x(n)
print(y)