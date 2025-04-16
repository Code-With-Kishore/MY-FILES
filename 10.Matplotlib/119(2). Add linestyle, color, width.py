# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 17:50:37 2025

@author: Admin
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']
y = df['TAMIL']

plt.plot(x, y, marker='o', ms=5, mec='red', mfc='yellow', color='green', linestyle='--', linewidth=2 )
plt.show()