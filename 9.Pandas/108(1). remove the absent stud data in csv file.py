# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:06:59 2025

@author: Admin
"""

import pandas as pd
df = pd.read_csv('D:\datasheet2.csv')
print(df)
df=df.dropna()
print(df)