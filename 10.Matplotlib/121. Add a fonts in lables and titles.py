# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 18:43:06 2025

@author: Admin
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']
y = df['TAMIL']

font={'family': 'Times New Roman',
      'color': 'Black',
      'size': 20}

plt.plot(x, y, '^--g' , mec='red', mfc='yellow' )
plt.xlabel('Roll.No of Student', fontdict=font)
plt.ylabel('Marks of Student', fontdict=font)
plt.title('Tamil Subject Mark', fontdict=font)
plt.show()