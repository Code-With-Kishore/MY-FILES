# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:00:23 2025

@author: Admin
"""

import pandas as pd
c=['NAME', 'MATHS']
df = pd.read_csv('D:\STUDENT MARKS2.csv', usecols=c)
print(df)