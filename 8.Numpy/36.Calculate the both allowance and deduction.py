# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:10:42 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
salary=np.random.randint(20000, 50000, n)

hra=salary*0.20
ta=salary*0.10
total_allowance=salary+hra+ta

PF=salary*0.12
IT=salary*0.05
total_detection=PF+IT

gross_sal = salary + total_allowance
net_salary = gross_sal - total_detection


print('Salary: ', salary)
print('HRA allowance: ', hra)
print('Travel allowance: ', ta)
print('PF: ',PF)
print('IT: ',IT)
print('Gross salary: ', gross_sal)
print('Net salary: ', net_salary)
