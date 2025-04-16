# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 11:37:48 2025

@author: Admin
"""

import matplotlib.pyplot as mp
import pandas as pd

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']
y = df['TAMIL']

font={'family': 'Times New Roman',
      'color': 'Black',
      'size': 18}

mp.scatter(x, y, marker='s', s=50, c=y, cmap='viridis', edgecolor='black')
mp.xlabel('Roll.Num', fontdict=font)
mp.ylabel('Marks', fontdict=font)
mp.title('Tamil Subject Marks', fontdict=font)
mp.grid(color='black', linestyle='--', linewidth=0.5)

mp.show()
