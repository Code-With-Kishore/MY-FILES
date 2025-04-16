# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:50:17 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
salary=np.random.randint(20000, 50000, n)
hra=salary*0.20
ta=salary*0.10
total_salary=salary+hra+ta
print('Salary: ', salary)
print('Total Salary: ',total_salary)
print('HRA allowance: ',hra)
print('Travel allowance: ',ta)