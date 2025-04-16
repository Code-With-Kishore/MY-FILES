# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 06:26:29 2024

@author: Admin
"""
import random
x=lambda n: [random.randint(1,100)for i in range(n)]
n=int(input('Enter n value:'))
list1=x(n)
list2=x(n)
print(list1)
print(list2)