# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:19:12 2025

@author: Admin
"""

import numpy as np

n = int(input("Enter the number of elements: "))

arr = np.random.randint(-100, 100, n)

single_digit_nums = arr[(arr >= -9) & (arr <= 9)]

print("Generated numbers:", arr)
print("Single-digit numbers:", single_digit_nums)

