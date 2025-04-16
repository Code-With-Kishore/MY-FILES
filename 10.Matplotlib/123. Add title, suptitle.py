# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 10:19:53 2025

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
mp.plot(x, y1)

mp.subplot(2, 3, 2)
mp.title('English')
mp.plot(x, y2)

mp.subplot(2, 3, 3)
mp.title('Maths')
mp.plot(x, y3)

mp.subplot(2, 3, 4)
mp.title('Science')
mp.plot(x, y4)

mp.subplot(2, 3, 5)
mp.title('Social')
mp.plot(x, y5)

mp.suptitle('All Subject Marks', fontdict=font)

mp.tight_layout()
mp.show()