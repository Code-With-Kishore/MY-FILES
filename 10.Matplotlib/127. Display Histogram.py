# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 18:22:18 2025

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']
y = df['ENGLISH']

font={'family': 'Times New Roman',
      'color': 'Black',
      'size': 18}

plt.hist(y, color='green')

plt.xlabel('Students Marks', fontdict=font)
plt.ylabel('Frequency', fontdict=font)

plt.title('English Subject Marks', fontdict=font)

plt.show()