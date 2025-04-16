# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 10:45:14 2025

@author: Admin
"""

import numpy as np

d = np.dtype({'names': ('Name', 'Age', 'Mark', 'Gender', 'Qualification', 'Location'), 
              'formats': ('U10', 'i4', 'f4', 'U10', 'U10', 'U20')})  

x = [('Krish', 23, 80.5, 'Male', 'M.Sc', 'Tiruchirappalli')]

data = np.array(x, d)

print(data)


