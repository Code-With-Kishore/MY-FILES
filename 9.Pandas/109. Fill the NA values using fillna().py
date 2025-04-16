# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 16:53:09 2025

@author: Admin
"""

import pandas as pd
df = pd.read_csv('D:\STUDENT MARKS2.csv')
print(df)
x=df.fillna(0)
print(x)