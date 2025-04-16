# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:04:37 2025

@author: Admin
"""

import pandas as pd
c=['ROLL.NO','NAME', 'MATHS']
df = pd.read_csv('D:\STUDENT MARKS2.csv', usecols=c, index_col='ROLL.NO')
print(df)