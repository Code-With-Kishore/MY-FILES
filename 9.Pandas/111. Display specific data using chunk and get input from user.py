# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:27:18 2025

@author: Admin
"""

import pandas as pd
ch_size=2
for chunk in pd.read_csv('D:\STUDENT MARKS2.csv', chunksize=ch_size):
    print(chunk)
    input('Enter next: ')