# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:35:48 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
salary=np.random.randint(20000, 100000, n)
PF=salary*0.12
IT=salary*0.05
total_detection=PF+IT
net_salary=salary-total_detection
print('Salary: ', salary)
print('PF: ',PF)
print('IT: ',IT)
print('Total Detection: ',total_detection)
print('Net salary: ', net_salary)