# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 17:28:35 2025

@author: Admin
"""

import matplotlib.pyplot as mp
import pandas as pd

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']

y1 = df['TAMIL']
y2 = df['ENGLISH']
y3 = df['MATHS']
y4 = df['SCIENCE']
y5 = df['SOCIAL']

font={'family': 'Times New Roman',
      'color': 'Black',
      'size': 22}

mp.subplot(2, 3, 1) # 3 Rows * 2 Cols
mp.title('Tamil')
mp.bar(x, y1, color='red')

mp.subplot(2, 3, 2)
mp.title('English')
mp.bar(x, y2, color='blue')

mp.subplot(2, 3, 3)
mp.title('Maths')
mp.bar(x, y3, color='green')

mp.subplot(2, 3, 4)
mp.title('Science')
mp.bar(x, y4, color='yellow')

mp.subplot(2, 3, 5)
mp.title('Social')
mp.bar(x, y5, color='purple')

mp.suptitle('All Subject Marks', fontdict=font)

mp.tight_layout()
mp.show()
