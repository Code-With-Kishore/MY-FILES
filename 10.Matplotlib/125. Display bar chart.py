# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 17:13:18 2025

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

plt.bar(x, y, color='green', width=0.5)
plt.xlabel('Students Roll Number', fontdict=font)
plt.ylabel('Students Marks', fontdict=font)
plt.title('English Subject Marks', fontdict=font)
plt.tight_layout()
plt.show()