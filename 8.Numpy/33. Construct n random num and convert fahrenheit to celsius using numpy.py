# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:34:48 2025

@author: Admin
"""

import numpy as np
n=int(input('Enter n value: '))
fahrenhiet=np.random.randint(0,1000,n)
celsius=5/9*(fahrenhiet-32)
print('Fahrenheit value: ',fahrenhiet)
print('Celsius value: ',celsius)
