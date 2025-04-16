# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 06:47:12 2024

@author: Admin
"""
import random
matrix=lambda n: [[random.randint(0,100)for i in range(n)]for j in range(n)]
n=int(input('Enter n value:'))
x=matrix(n)
print(x)