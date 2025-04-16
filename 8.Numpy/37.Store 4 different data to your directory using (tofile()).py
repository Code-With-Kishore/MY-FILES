# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:37:41 2025

@author: Admin
"""

import numpy as np

n=int(input('Enter n data value: '))

f1=np.random.randint(50, 100, n, dtype='uint8')
f2=np.random.randint(50, 100, n, dtype='uint8')
f3=np.random.randint(50, 100, n, dtype='uint8')
f4=np.random.randint(50, 100, n, dtype='uint8')

mark1=open('C:/Users/Admin/Documents/Python/Data Science/m1', 'wb')
mark2=open('C:/Users/Admin/Documents/Python/Data Science/m2', 'wb')
seminar=open('C:/Users/Admin/Documents/Python/Data Science/seminarfile', 'wb')
attendence=open('C:/Users/Admin/Documents/Python/Data Science/attendencefile', 'wb')

f1.tofile(mark1)
f2.tofile(mark2)
f3.tofile(seminar)
f4.tofile(attendence)

print('file saved successfully...')

